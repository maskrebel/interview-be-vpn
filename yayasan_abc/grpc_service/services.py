from django.contrib.auth.models import User

from . import user_pb2, user_pb2_grpc


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
