import json

from django.conf import settings
from django.shortcuts import render, redirect
from rest_framework.views import APIView
import requests


class HomeView(APIView):
    def get(self, request):
        access_token = request.COOKIES.get('access_token')
        contexts = {'sso_url' : settings.URL_SSO_ROOT}
        if access_token:
            try:
                headers = {
                    'token': f'{access_token}',
                }

                response = requests.request("GET", settings.URL_SSO_USER_INFO, headers=headers)

                data = json.loads(response.text)
                user = data['user']

                contexts['user'] = user

            except Exception as e:
                pass

        return render(request, 'user/home.html', contexts)


class SSOLogoutView(APIView):
    def post(self, request):
        token = request.COOKIES.get('access_token')
        response = redirect('/')
        if token:
            response.delete_cookie('access_token')
        return response
