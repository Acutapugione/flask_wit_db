from .. import Base
from sqlalchemy.orm import Mapped, mapped_column,  relationship
from sqlalchemy import ForeignKey


class Student(Base):
    name: Mapped[str]
    
    group: Mapped["Group"] = relationship(back_populates="students")
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"))