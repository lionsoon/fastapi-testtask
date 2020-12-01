from fastapi import APIRouter
from uuid import UUID

from database.crud import find_managers, all_managers
from .scope import db_manager
from typing import List
from database.models import Manager, DetailManager

router = APIRouter()


@router.get("/managers/list", response_model=List[DetailManager])
async def list_all_managers():
    async with db_manager.session() as session:
        return await all_managers(session=session)

@router.get("/managers/{user_id}", response_model=List[Manager])
async def managers(user_id: UUID):
    async with db_manager.session() as session:
        return await find_managers(user_id, session=session)

