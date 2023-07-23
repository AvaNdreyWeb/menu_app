from sqlalchemy import Column, String

from .database import Base


class Menu(Base):
    __tablename__ = "menus"

    id = Column(String, primary_key=True)
    title = Column(String)
    description = Column(String)
