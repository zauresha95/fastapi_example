from fastapi import APIRouter, BackgroundTasks, Depends
from typing import List, Optional

from .schemas import SUser
from .dao import UserDAO

router = APIRouter(
    prefix='/users',
    tags=['USERS']
)


@router.get('{id}')
async def get_users(
        user_id: int
) -> Optional[List[SUser]]:
    users = await UserDAO.find_by_id(id=user_id)
    return users


@router.post('')
async def add_users(user: SUser):
    users = await UserDAO.add(
        id=user.id,
        name=user.name,
        surname=user.surname,
        email=user.email,
        birthday=user.birthday
    )
    return users

