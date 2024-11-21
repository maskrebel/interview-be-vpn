from concurrent import futures
import time

import django
import grpc

from grpc_service import user_pb2, user_pb2_grpc

# need initial for run django service
django.setup()

from grpc_service.services import UserService


def grpc_server():
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
