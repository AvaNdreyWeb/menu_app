from pydantic import BaseModel


class InfoMessage(BaseModel):
    status: bool
    message: str


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MENUS
class CreateMenuDTO(BaseModel):
    title: str
    description: str


class Menu(CreateMenuDTO):
    id: str

    class Config:
        orm_mode = True


class MenuDTO(Menu):
    submenus_count: int
    dishes_count: int


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ SUBMENUS
class CreateSubmenuDTO(BaseModel):
    title: str
    description: str


class Submenu(CreateSubmenuDTO):
    id: str

    class Config:
        orm_mode = True


class SubmenuDTO(Submenu):
    dishes_count: int


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DISHES
class CreateDishDTO(BaseModel):
    title: str
    description: str
    price: str


class Dish(CreateDishDTO):
    id: str
    price: float

    class Config:
        orm_mode = True


class DishDTO(Dish):
    price: str
