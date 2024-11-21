import time

import django
from concurrent import futures
import grpc

from . import user_pb2, user_pb2_grpc

django.setup()

from django.contrib.auth.models import User


class UserService(user_pb2_grpc.UserServiceServicer):
    def ListUsers(self, request, context):
        users = User.objects.all()

        user_list = []
        for user in users:user_list.append(user_pb2.User(
                id=user.id,
                username=user.username,
                email=user.email,
                fullname=f'{user.first_name} {user.last_name}',
            ))

        return user_pb2.UserList(users=user_list)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)

    server.add_insecure_port('[::]:50051')
    print('gRPC server running on port 50051...')
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)