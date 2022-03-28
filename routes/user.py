from fastapi import APIRouter

user = APIRouter()

@user.get('/')
def helloword():
    return ("hello world")