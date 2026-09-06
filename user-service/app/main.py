import grpc

from fastapi import FastAPI

from app import profile_pb2
from app import profile_pb2_grpc


app = FastAPI()


channel = grpc.insecure_channel("localhost:50051")

profile_client = profile_pb2_grpc.ProfileServiceStub(channel)


@app.get("/users/{user_id}")
def get_user(user_id: int):

    request = profile_pb2.ProfileRequest(
        user_id=user_id
    )

    response = profile_client.GetProfile(request)

    return {
        "id": response.user_id,
        "name": response.name,
        "email": response.email
    }
