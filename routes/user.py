from fastapi import APIRouter

user = APIRouter()

@user.get('/')
def helloword():
    print("hello world")