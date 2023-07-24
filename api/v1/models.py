from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class Menu(Base):
    __tablename__ = "menus"

    id = Column(String, primary_key=True)
    title = Column(String)
    description = Column(String)

    submenus = relationship(
        "Submenu", back_populates="menu", cascade="all, delete-orphan"
    )


class Submenu(Base):
    __tablename__ = "submenus"

    id = Column(String, primary_key=True)
    title = Column(String)
    description = Column(String)
    menu_id = Column(String, ForeignKey("menus.id"))

    menu = relationship("Menu", back_populates="submenus")
    dishes = relationship(
        "Dish", back_populates="submenu", cascade="all, delete-orphan"
    )


class Dish(Base):
    __tablename__ = "dishes"

    id = Column(String, primary_key=True)
    title = Column(String)
    description = Column(String)
    price = Column(Float)
    submenu_id = Column(String, ForeignKey("submenus.id"))

    submenu = relationship("Submenu", back_populates="dishes")
