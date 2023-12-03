from fastapi import APIRouter, Depends
from .schemas import Signin, Signup
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
    email = req_body.email
    password = req_body.password
    print(email, " ", password)
    # async with session.begin() as session:
    #     new_user = Register(email=email, password=password)
    #     session.add(new_user)
    #     await session.commit()
    registerRepository = RegisterRepository(session=session)
    created_user = await registerRepository.create_user(email=email, password=password)
    print("Created user:", created_user)
    print(type(created_user))
    for val in created_user:
        print("val: ", val)
    return "hello world"

    # return "hello world from auth / sign up "
