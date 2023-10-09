from sqlalchemy import select, insert

from app.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def find_by_id(cls, id):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def add(cls, *args, **kwargs):
        async with async_session_maker() as session:
            query = insert(cls.model).values(*args, **kwargs)
            result = await session.execute(query)
            await session.commit()
            return result.scalar_one_or_none()