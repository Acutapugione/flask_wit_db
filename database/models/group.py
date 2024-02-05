from .. import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List


class Group(Base):
    name: Mapped[str]
    students: Mapped[List["Student"]] = relationship(back_populates="group")
    lessons: Mapped[List["Lesson"]] = relationship(back_populates="group")