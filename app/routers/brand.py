from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.brand import Brand, BrandStatus
from app.schemas.brand import BrandCreate, Brand as BrandSchema

router = APIRouter()


@router.get("/", response_model=List[BrandSchema])
def get_brands(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtener lista de marcas"""
    brands = db.query(Brand).offset(skip).limit(limit).all()
    return brands


@router.get("/{brand_id}", response_model=BrandSchema)
def get_brand(brand_id: int, db: Session = Depends(get_db)):
    """Obtener una marca por ID"""
    brand = db.query(Brand).filter(Brand.id == brand_id).first()
    if brand is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Marca no encontrada"
        )
    return brand


@router.post("/", response_model=BrandSchema, status_code=status.HTTP_201_CREATED)
def create_brand(brand: BrandCreate, db: Session = Depends(get_db)):
    """Crear una nueva marca"""
    if brand.registration_number:
        existing_brand = (
            db.query(Brand)
            .filter(Brand.registration_number == brand.registration_number)
            .first()
        )
        if existing_brand:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe una marca con este número de registro",
            )

    db_brand = Brand(**brand.model_dump())
    db.add(db_brand)
    db.commit()
    db.refresh(db_brand)
    return db_brand


@router.put("/{brand_id}", response_model=BrandSchema)
def update_brand(brand_id: int, brand: BrandCreate, db: Session = Depends(get_db)):
    """Actualizar una marca existente"""
    db_brand = db.query(Brand).filter(Brand.id == brand_id).first()
    if db_brand is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Marca no encontrada"
        )

    if (
        brand.registration_number
        and brand.registration_number != db_brand.registration_number
    ):
        existing_brand = (
            db.query(Brand)
            .filter(Brand.registration_number == brand.registration_number)
            .first()
        )
        if existing_brand:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe una marca con este número de registro",
            )

    for key, value in brand.model_dump().items():
        setattr(db_brand, key, value)

    db.commit()
    db.refresh(db_brand)
    return db_brand


@router.delete("/{brand_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_brand(brand_id: int, db: Session = Depends(get_db)):
    """Eliminar una marca"""
    db_brand = db.query(Brand).filter(Brand.id == brand_id).first()
    if db_brand is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Marca no encontrada"
        )

    db.delete(db_brand)
    db.commit()
    return None


@router.get("/status/{status}", response_model=List[BrandSchema])
def get_brands_by_status(status: BrandStatus, db: Session = Depends(get_db)):
    """Obtener marcas por estado"""
    brands = db.query(Brand).filter(Brand.status == status).all()
    return brands
