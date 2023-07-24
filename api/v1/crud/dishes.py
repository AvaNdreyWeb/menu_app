import uuid

from sqlalchemy.orm import Session

from .. import models, schemas


def get_all(db: Session, submenu_id: str):
    db_dishes_list = db.query(models.Dish).filter(
        models.Dish.submenu_id == submenu_id
    )
    dishes_dto_list = []
    for db_dish in db_dishes_list:
        dish_dto = schemas.DishDTO(
            id=db_dish.id,
            title=db_dish.title,
            description=db_dish.description,
            price=f"{db_dish.price:.2f}"
        )
        dishes_dto_list.append(dish_dto)
    return dishes_dto_list


def get_by_id(db: Session, submenu_id: str, dish_id: str):
    db_dish = db.query(models.Dish).filter(
        models.Dish.submenu_id == submenu_id,
        models.Dish.id == dish_id
    ).first()
    if db_dish:
        dish_dto = schemas.DishDTO(
            id=db_dish.id,
            title=db_dish.title,
            description=db_dish.description,
            price=f"{db_dish.price:.2f}"
        )
        return dish_dto
    return None


def create(db: Session, submenu_id: str, dish_data: schemas.CreateDishDTO):
    dish_id = str(uuid.uuid4())
    dish = schemas.Dish(
        id=dish_id,
        title=dish_data.title,
        description=dish_data.description,
        price=float(dish_data.price)
    )
    db_dish = models.Dish(**dish.model_dump(), submenu_id=submenu_id)
    db.add(db_dish)
    db.commit()
    db.refresh(db_dish)

    dish_dto = schemas.DishDTO(
        id=dish.id,
        title=dish.title,
        description=dish.description,
        price=f"{dish.price:.2f}"
    )
    return dish_dto


def update(
        db: Session,
        submenu_id: str,
        dish_id: str,
        dish_data: schemas.CreateDishDTO
):
    db_dish = db.query(models.Dish).filter(
        models.Dish.submenu_id == submenu_id,
        models.Dish.id == dish_id
    ).first()
    if not db_dish:
        return None

    db_dish.title = dish_data.title
    db_dish.description = dish_data.description
    db_dish.price = float(dish_data.price)

    db.add(db_dish)
    db.commit()
    db.refresh(db_dish)

    dish_dto = schemas.DishDTO(
        id=db_dish.id,
        title=db_dish.title,
        description=db_dish.description,
        price=f"{db_dish.price:.2f}"
    )
    return dish_dto


def delete(db: Session, submenu_id: str, dish_id: str):
    db_dish = db.query(models.Dish).filter(
        models.Dish.submenu_id == submenu_id,
        models.Dish.id == dish_id
    ).first()
    if db_dish:
        db.delete(db_dish)
        db.commit()
