from app.Models.Register import Register
from app.Core.db import AsyncSession
from sqlalchemy import select
from .schemas import User


class RegisterRepository:
    def __init__(self, session: AsyncSession):
        self.async_session = session

    async def read_by_id(self, register_id: int):
        async with self.async_session.begin() as session:
            stmt = select(Register).where(Register.id == register_id)
            result = await session.scalar(stmt)
            return result

    async def create_user(self, email: str, password: str):
        async with self.async_session.begin() as session:
            new_user = Register(email=email, password=password)
            session.add(new_user)
            await session.flush()





