import uuid

from sqlalchemy.orm import Session

from .. import models, schemas


def get_all(db: Session):
    db_menu_list = db.query(models.Menu).all()
    menu_dto_list = []
    for db_menu in db_menu_list:
        submenus_count = len(db_menu.submenus)
        dishes_count = sum([len(sub.dishes) for sub in db_menu.submenus])
        menu_dto = schemas.MenuDTO(
            id=db_menu.id,
            title=db_menu.title,
            description=db_menu.description,
            submenus_count=submenus_count,
            dishes_count=dishes_count
        )
        menu_dto_list.append(menu_dto)
    return menu_dto_list


def get_by_id(db: Session, menu_id: str):
    db_menu = db.query(models.Menu).filter(models.Menu.id == menu_id).first()
    if db_menu:
        submenus_count = len(db_menu.submenus)
        dishes_count = sum([len(sub.dishes) for sub in db_menu.submenus])
        menu_dto = schemas.MenuDTO(
            id=db_menu.id,
            title=db_menu.title,
            description=db_menu.description,
            submenus_count=submenus_count,
            dishes_count=dishes_count
        )
        return menu_dto
    return None


def create(db: Session, menu_data: schemas.CreateMenuDTO):
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


def update(db: Session, menu_id: str, menu_data: schemas.CreateMenuDTO):
    db_menu = db.query(models.Menu).filter(models.Menu.id == menu_id).first()
    if not db_menu:
        return None

    db_menu.title = menu_data.title
    db_menu.description = menu_data.description

    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)

    submenus_count = len(db_menu.submenus)
    dishes_count = sum([len(sub.dishes) for sub in db_menu.submenus])
    menu_dto = schemas.MenuDTO(
        id=db_menu.id,
        title=db_menu.title,
        description=db_menu.description,
        submenus_count=submenus_count,
        dishes_count=dishes_count
    )
    return menu_dto


def delete(db: Session, menu_id: str):
    db_menu = db.query(models.Menu).filter(models.Menu.id == menu_id).first()
    if db_menu:
        db.delete(db_menu)
        db.commit()
