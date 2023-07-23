import uuid

from sqlalchemy.orm import Session

from . import models, schemas


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MENUS
def get_menu_list(db: Session):
    db_menu_list = db.query(models.Menu).all()
    menu_dto_list = []
    for db_menu in db_menu_list:
        submenus_count = 0  # TODO
        dishes_count = 0  # TODO
        menu = schemas.MenuDTO(
            id=db_menu.id,
            title=db_menu.title,
            description=db_menu.description,
            submenus_count=submenus_count,
            dishes_count=dishes_count
        )
        menu_dto_list.append(menu)
    return menu_dto_list


def get_menu(db: Session, menu_id: str):
    db_menu = db.query(models.Menu).filter(models.Menu.id == menu_id).first()
    if db_menu:
        submenus_count = 0  # TODO
        dishes_count = 0  # TODO
        menu = schemas.MenuDTO(
            id=db_menu.id,
            title=db_menu.title,
            description=db_menu.description,
            submenus_count=submenus_count,
            dishes_count=dishes_count
        )
        return menu
    return None


def create_menu(db: Session, menu_data: schemas.CreateMenuDTO):
    menu_id = str(uuid.uuid4())
    menu = schemas.Menu(
        id=menu_id,
        title=menu_data.title,
        description=menu_data.description
    )
    db_menu = models.Menu(**menu.model_dump())
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)

    menu_dto = schemas.MenuDTO(
        id=menu.id,
        title=menu.title,
        description=menu.description,
        submenus_count=0,
        dishes_count=0
    )
    return menu_dto


def update_menu(db: Session, menu_id: str, menu_data: schemas.CreateMenuDTO):
    db_menu = db.query(models.Menu).filter(models.Menu.id == menu_id).first()
    if not db_menu:
        return None

    db_menu.title = menu_data.title
    db_menu.description = menu_data.description

    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)

    submenus_count = 0  # TODO
    dishes_count = 0  # TODO
    menu_dto = schemas.MenuDTO(
        id=db_menu.id,
        title=db_menu.title,
        description=db_menu.description,
        submenus_count=submenus_count,
        dishes_count=dishes_count
    )
    return menu_dto


def delete_menu(db: Session, menu_id: str):
    db_menu = db.query(models.Menu).filter(models.Menu.id == menu_id).first()
    if db_menu:
        db.delete(db_menu)
        db.commit()
