from app.Core.db import Base, async_engine
import asyncio


async def create_db():
    async with async_engine.begin() as connection:
        from app.Models.User import User

        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)
    await async_engine.dispose()


asyncio.run(create_db())
