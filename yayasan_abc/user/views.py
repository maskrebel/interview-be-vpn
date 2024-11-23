from django.shortcuts import render
import grpc
from grpc_service import user_pb2, user_pb2_grpc
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import InvalidToken
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
