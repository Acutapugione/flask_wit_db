from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.orm import Mapped, mapped_column

engine = create_engine('sqlite:///my_db.sql', echo=True)

Session = sessionmaker(engine)

class Base(DeclarativeBase):
    id:Mapped[int] = mapped_column(primary_key=True)
    
    def __repr__(self) -> str:
        if hasattr(self, "name"):
            return f"{self.__class__.__name__.lower()}: {self.name}"
        
        return super().__repr__()
    
    @classmethod
    @property
    def __tablename__(cls):
        return cls.__name__.lower() + "s"


from . import models


def migrate_up():
    Base.metadata.drop_all(engine)
    
    Base.metadata.create_all(engine)
    
    with Session.begin() as session:
        group = models.Group(name="1y_2_23")
        students = [
            models.Student(name="Vasya", group=group),
            models.Student(name="Petya", group=group),
        ]
        session.add_all(students)