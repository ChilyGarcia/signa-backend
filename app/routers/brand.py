from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.dependencies.repositories import get_brand_repository
from app.repositories.brand import BrandRepository
from app.models.brand import BrandStatus
from app.schemas.brand import BrandCreate, BrandUpdate, Brand as BrandSchema

router = APIRouter()


@router.get("/", response_model=List[BrandSchema])
def get_brands(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    brand_repo: BrandRepository = Depends(get_brand_repository),
):
    """Obtener lista de marcas"""
    return brand_repo.get_all(db, skip=skip, limit=limit)


@router.get("/{brand_id}", response_model=BrandSchema)
def get_brand(
    brand_id: int,
    db: Session = Depends(get_db),
    brand_repo: BrandRepository = Depends(get_brand_repository),
):
    """Obtener una marca por ID"""
    brand = brand_repo.get(db, brand_id)
    if brand is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Brand not found"
        )
    return brand


@router.post("/", response_model=BrandSchema, status_code=status.HTTP_201_CREATED)
def create_brand(
    brand: BrandCreate,
    db: Session = Depends(get_db),
    brand_repo: BrandRepository = Depends(get_brand_repository),
):
    """Crear una nueva marca"""
    if brand.registration_number:
        if brand_repo.exists_by_registration_number(db, brand.registration_number):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="A brand with this registration number already exists",
            )

    return brand_repo.create(db, obj_in=brand)


@router.put("/{brand_id}", response_model=BrandSchema)
def update_brand(
    brand_id: int,
    brand: BrandUpdate,
    db: Session = Depends(get_db),
    brand_repo: BrandRepository = Depends(get_brand_repository),
):
    """Actualizar una marca existente"""
    db_brand = brand_repo.get(db, brand_id)
    if db_brand is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Brand not found"
        )

    if (
        brand.registration_number
        and brand.registration_number != db_brand.registration_number
    ):
        if brand_repo.exists_by_registration_number(db, brand.registration_number):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="A brand with this registration number already exists",
            )

    return brand_repo.update(db, db_obj=db_brand, obj_in=brand)


@router.delete("/{brand_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_brand(
    brand_id: int,
    db: Session = Depends(get_db),
    brand_repo: BrandRepository = Depends(get_brand_repository),
):
    """Eliminar una marca"""
    db_brand = brand_repo.get(db, brand_id)
    if db_brand is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Brand not found"
        )

    brand_repo.remove(db, id=brand_id)
    return None


@router.get("/status/{status}", response_model=List[BrandSchema])
def get_brands_by_status(
    status: BrandStatus,
    db: Session = Depends(get_db),
    brand_repo: BrandRepository = Depends(get_brand_repository),
):
    """Obtener marcas por estado"""
    return brand_repo.get_by_status(db, status)


@router.get("/owner/{owner}", response_model=List[BrandSchema])
def get_brands_by_owner(
    owner: str,
    db: Session = Depends(get_db),
    brand_repo: BrandRepository = Depends(get_brand_repository),
):
    """Obtener marcas por propietario"""
    return brand_repo.get_by_owner(db, owner)


@router.get("/search/{name}", response_model=List[BrandSchema])
def search_brands_by_name(
    name: str,
    db: Session = Depends(get_db),
    brand_repo: BrandRepository = Depends(get_brand_repository),
):
    """Buscar marcas por nombre"""
    return brand_repo.search_by_name(db, name)


@router.get("/active/list", response_model=List[BrandSchema])
def get_active_brands(
    db: Session = Depends(get_db),
    brand_repo: BrandRepository = Depends(get_brand_repository),
):
    """Obtener solo marcas registradas (activas)"""
    return brand_repo.get_active_brands(db)


@router.patch("/{brand_id}/status", response_model=BrandSchema)
def update_brand_status(
    brand_id: int,
    status: BrandStatus,
    db: Session = Depends(get_db),
    brand_repo: BrandRepository = Depends(get_brand_repository),
):
    """Actualizar solo el estado de una marca"""
    brand = brand_repo.update_status(db, brand_id, status)
    if brand is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Brand not found"
        )
    return brand
