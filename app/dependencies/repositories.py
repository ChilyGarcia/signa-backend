from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.brand import BrandRepository


def get_brand_repository() -> BrandRepository:
    """Dependency para obtener el repositorio de Brand"""
    return BrandRepository()


def get_brand_repository_with_db(
    db: Session = Depends(get_db)
) -> BrandRepository:
    """Dependency para obtener el repositorio de Brand con sesión de DB"""
    return BrandRepository()
