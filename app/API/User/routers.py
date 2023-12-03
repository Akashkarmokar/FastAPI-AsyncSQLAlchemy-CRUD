from fastapi import APIRouter, Depends
from .schemas import Signin, Signup, User
from app.Core.db import AsyncSession
from app.Models.Register import Register
from app.API.User.register_repository import RegisterRepository

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
async def sign_up(req_body: Signup, session: AsyncSession):
    user_repository = RegisterRepository(session=session)
    created_user = await user_repository.create_user(email=req_body.email, password=req_body.password)
    ok = created_user
    return f'{created_user.id}'
    return "Created Successfully !!"


@UserRouter.get('/user/{user_id}')
async def get_user_by_id(user_id: int, session: AsyncSession):
    user_repository = RegisterRepository(session=session)
    user = await user_repository.read_by_id(user_id)

    return f"{ user.id } {user.email}"
