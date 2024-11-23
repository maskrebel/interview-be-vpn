from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate
import grpc
from grpc_service import user_pb2, user_pb2_grpc
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication


class Users(APIView):
    def get(self, request):
        users = self.list_users()
        return Response(users)

    def list_users(self):
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = user_pb2_grpc.UserServiceStub(channel)
            response = stub.ListUsers(user_pb2.Empty())

            users = []
            for user in response.users:
                users.append({
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'fullname': user.fullname,
                })
            return users


class HomeView(APIView):
    def get(self, request):
        access_token = request.COOKIES.get('access_token')
        contexts = {}
        response = render(request, 'user/home.html', contexts)
        if access_token:
            try:
                token = JWTAuthentication().get_validated_token(access_token)
                user = JWTAuthentication().get_user(token)
                contexts['user'] = user
                response = render(request, 'user/home.html', contexts)

            except InvalidToken:
                response.delete_cookie('access_token')

        return response


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
                httponly=True,
                secure=settings.SECURE_COOKIES,
                max_age=3600
            )

            return response
        else:
            return render(request, 'user/login.html', {'error': 'Invalid username or password.'})


class SSOLogoutView(APIView):
    def post(self, request):
        token = request.COOKIES.get('access_token')
        response = redirect('/')
        if token:
            response.delete_cookie('access_token')
        return response

class UserInfo(APIView):
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