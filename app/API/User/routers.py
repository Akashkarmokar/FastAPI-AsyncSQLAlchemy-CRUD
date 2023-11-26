from fastapi import APIRouter
from .schemas import Signin, Signup

UserRouter = APIRouter(tags=['Auth'], prefix='/auth')


@UserRouter.get('/')
async def get_user():
    return {
        'status_code': 200,
        'message': 'Data is fetched successfully !!',
        'data': {
            'name': 'Hello User',
            'email': 'hello@example.com'
        }
    }


@UserRouter.post('/signin')
async def sign_in(req_body: Signin):
    return req_body


@UserRouter.post('/signup')
async def sign_up(req_body: Signup):
    return req_body
