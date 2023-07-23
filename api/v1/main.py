from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from . import crud, database, schemas

BASE_PATH = '/api/v1'
database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MENUS
@app.get(
        f'{BASE_PATH}/menus',
        response_model=list[schemas.MenuDTO],
        status_code=status.HTTP_200_OK
)
def get_menu_list(db: Session = Depends(get_db)):
    menu_list = crud.get_menu_list(db)
    return menu_list


@app.get(
        f'{BASE_PATH}/menus/{{menu_id}}',
        response_model=schemas.MenuDTO,
        status_code=status.HTTP_200_OK
)
def get_menu(menu_id: str, db: Session = Depends(get_db)):
    menu = crud.get_menu(db, menu_id)
    if not menu:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "menu not found")
    return menu


@app.post(
        f'{BASE_PATH}/menus',
        response_model=schemas.MenuDTO,
        status_code=status.HTTP_201_CREATED
)
def create_menu(
    menu_data: schemas.CreateMenuDTO, db: Session = Depends(get_db)
):
    menu = crud.create_menu(db, menu_data)
    return menu


@app.patch(
        f'{BASE_PATH}/menus/{{menu_id}}',
        response_model=schemas.MenuDTO,
        status_code=status.HTTP_200_OK
)
def update_menu(
    menu_id: str,
    menu_data: schemas.CreateMenuDTO,
    db: Session = Depends(get_db)
):
    menu = crud.update_menu(db, menu_id, menu_data)
    if not menu:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "menu not found")
    return menu


@app.delete(
        f'{BASE_PATH}/menus/{{menu_id}}',
        response_model=schemas.InfoMessage,
        status_code=status.HTTP_200_OK
)
def delete_menu(menu_id: str, db: Session = Depends(get_db)):
    crud.delete_menu(db, menu_id)
    return schemas.InfoMessage(
        status=True, message="The menu has been deleted"
    )
