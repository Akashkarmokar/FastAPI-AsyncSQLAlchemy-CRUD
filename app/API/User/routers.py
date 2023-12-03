from fastapi import APIRouter, Depends
from .schemas import Signin, Signup, User
from app.Core.db import AsyncSession
from app.Models.Register import Register
from app.API.User.register_repository import RegisterRepository
from sqlalchemy import select

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
    # async with session.begin() as session:
    #     new_user = Register(email=req_body.email, password=req_body.password)
    #     session.add(new_user)
    #     await session.flush()
    #
    #     stmt = select(Register).where(Register.id == new_user.id)
    #     result = await session.scalar(stmt)
    #
    #     return User.model_validate(result)
    user_repository = RegisterRepository(session=session)
    created_user = await user_repository.create_user(email=req_body.email, password=req_body.password)
    print("From route: ", created_user)
    return "h"







@UserRouter.get('/user/{user_id}')
async def get_user_by_id(user_id: int, session: AsyncSession):
    user_repository = RegisterRepository(session=session)
    user = await user_repository.read_by_id(user_id)

    return f"{ user.id } {user.email}"
