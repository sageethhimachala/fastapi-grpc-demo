from concurrent import futures

import grpc

import profile_pb2
import profile_pb2_grpc


class ProfileService(profile_pb2_grpc.ProfileServiceServicer):

    def GetProfile(self, request, context):

        print(f"Received request for user: {request.user_id}")

        return profile_pb2.ProfileResponse(
            user_id=request.user_id,
            name="Sageeth",
            email="sageeth@example.com"
        )


def serve():

    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10)
    )

    profile_pb2_grpc.add_ProfileServiceServicer_to_server(
        ProfileService(),
        server
    )

    server.add_insecure_port("0.0.0.0:50051")

    server.start()

    print("Profile Service started")
    print("gRPC server listening on port 50051")

    server.wait_for_termination()


if __name__ == "__main__":
    serve()
