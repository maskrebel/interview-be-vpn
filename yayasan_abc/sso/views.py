from django.conf import settings
from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.tokens import RefreshToken

from .helpers import IsAuthenticated


class SSOLoginView(APIView):
    def get(self, request):
        return render(request, 'user/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        redirectURI = request.POST.get('redirectURI') or '/'

        user = authenticate(request, username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            response = redirect(redirectURI)

            response.set_cookie(
                'access_token', access_token,
                secure=settings.ACCESS_TOKEN_SECURE_COOKIES,
                max_age=3600,
                domain=settings.ACCESS_TOKEN_DOMAIN,
            )

            return response
        else:
            return render(request, 'user/login.html', {'error': 'Invalid username or password.'})


class SSOLogoutView(APIView):
    def post(self, request):
        token = request.COOKIES.get('access_token')
        response = redirect('/')
        if token:
            response.delete_cookie('access_token', domain=settings.ACCESS_TOKEN_DOMAIN)
        return response


class UserInfo(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        access_token = request.headers.get('token')
        res = {'is_success': False, 'user': ''}
        try:
            token = JWTAuthentication().get_validated_token(access_token)
            user = JWTAuthentication().get_user(token)
            res['is_success'] = True
            res['user'] = {'username': user.username, 'fullname': f'{user.first_name} {user.last_name}'}
        except InvalidToken:
            pass

        return Response(res)
