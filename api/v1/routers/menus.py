from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import schemas
from ..crud import menus
from ..dependencies import get_db

router = APIRouter(prefix="/menus", tags=["menus"])


@router.get(
        "",
        response_model=list[schemas.MenuDTO],
        status_code=status.HTTP_200_OK
)
def get_menu_list(db: Session = Depends(get_db)):
    menu_list = menus.get_all(db)
    return menu_list


@router.get(
        "/{menu_id}",
        response_model=schemas.MenuDTO,
        status_code=status.HTTP_200_OK
)
def get_menu(menu_id: str, db: Session = Depends(get_db)):
    menu = menus.get_by_id(db, menu_id)
    if not menu:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "menu not found")
    return menu


@router.post(
        "",
        response_model=schemas.MenuDTO,
        status_code=status.HTTP_201_CREATED
)
def create_menu(
    menu_data: schemas.CreateMenuDTO, db: Session = Depends(get_db)
):
    menu = menus.create(db, menu_data)
    return menu


@router.patch(
        "/{menu_id}",
        response_model=schemas.MenuDTO,
        status_code=status.HTTP_200_OK
)
def update_menu(
    menu_id: str,
    menu_data: schemas.CreateMenuDTO,
    db: Session = Depends(get_db)
):
    menu = menus.update(db, menu_id, menu_data)
    if not menu:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "menu not found")
    return menu


@router.delete(
        "/{menu_id}",
        response_model=schemas.InfoMessage,
        status_code=status.HTTP_200_OK
)
def delete_menu(menu_id: str, db: Session = Depends(get_db)):
    menus.delete(db, menu_id)
    return schemas.InfoMessage(
        status=True, message="The menu has been deleted"
    )
