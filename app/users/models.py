from datetime import date
from sqlalchemy.orm import mapped_column, Mapped
from app.database import Base


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    surname: Mapped[str]
    email: Mapped[str]
    birthday: Mapped[date]

    def __str__(self):
        return f"User {self.name} {self.surname}"
