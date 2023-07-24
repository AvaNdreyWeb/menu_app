from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import schemas
from ..crud import submenus
from ..dependencies import get_db

router = APIRouter(prefix="/menus/{menu_id}/submenus", tags=["submenus"])


@router.get(
        "",
        response_model=list[schemas.SubmenuDTO],
        status_code=status.HTTP_200_OK
)
def get_submenu_list(menu_id: str, db: Session = Depends(get_db)):
    submenu_list = submenus.get_all(db, menu_id)
    return submenu_list


@router.get(
        "/{submenu_id}",
        response_model=schemas.SubmenuDTO,
        status_code=status.HTTP_200_OK
)
def get_submenu(menu_id: str, submenu_id: str, db: Session = Depends(get_db)):
    submenu = submenus.get_by_id(db, menu_id, submenu_id)
    if not submenu:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "submenu not found")
    return submenu


@router.post(
        "",
        response_model=schemas.SubmenuDTO,
        status_code=status.HTTP_201_CREATED
)
def create_submenu(
    menu_id: str,
    submenu_data: schemas.CreateSubmenuDTO,
    db: Session = Depends(get_db)
):
    submenu = submenus.create(db, menu_id, submenu_data)
    return submenu


@router.patch(
        "/{submenu_id}",
        response_model=schemas.SubmenuDTO,
        status_code=status.HTTP_200_OK
)
def update_submenu(
    menu_id: str,
    submenu_id: str,
    submenu_data: schemas.CreateSubmenuDTO,
    db: Session = Depends(get_db)
):
    submenu = submenus.update(db, menu_id, submenu_id, submenu_data)
    if not submenu:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "submenu not found")
    return submenu


@router.delete(
        "/{submenu_id}",
        response_model=schemas.InfoMessage,
        status_code=status.HTTP_200_OK
)
def delete_submenu(
    menu_id: str, submenu_id: str, db: Session = Depends(get_db)
):
    submenus.delete(db, menu_id, submenu_id)
    return schemas.InfoMessage(
        status=True, message="The submenu has been deleted"
    )
