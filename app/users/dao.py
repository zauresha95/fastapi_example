from os.path import abspath, dirname
import sys
sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))

from app.dao.base import BaseDAO
from .models import User


class UserDAO(BaseDAO):
    model = User

    # @classmethod
    # async def add(cls):
    #     pass