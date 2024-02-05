from .. import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


class Lesson(Base):
    subject:Mapped[str]
    
    group: Mapped["Group"] = relationship(back_populates="lessons")
    group_id:Mapped[int] = mapped_column(ForeignKey("groups.id"))