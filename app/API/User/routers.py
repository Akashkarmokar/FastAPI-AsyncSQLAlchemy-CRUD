from fastapi import APIRouter

UserRouter = APIRouter(tags=['User'], prefix='/user')


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
