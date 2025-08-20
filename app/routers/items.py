from fastapi import APIRouter
from app.schemas.item import Item

router = APIRouter()


@router.get("/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@router.post("/")
def create_item(item: Item):
    return item
