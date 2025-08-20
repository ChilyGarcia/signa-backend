from typing import List, Optional
from sqlalchemy.orm import Session

from app.repositories.base import BaseRepository
from app.models.brand import Brand, BrandStatus
from app.schemas.brand import BrandCreate, BrandUpdate


class BrandRepository(BaseRepository[Brand, BrandCreate, BrandUpdate]):

    def __init__(self):
        super().__init__(Brand)

    def get_by_registration_number(
        self, db: Session, registration_number: str
    ) -> Optional[Brand]:
        return (
            db.query(Brand)
            .filter(Brand.registration_number == registration_number)
            .first()
        )

    def get_by_status(self, db: Session, status: BrandStatus) -> List[Brand]:
        return db.query(Brand).filter(Brand.status == status).all()

    def get_by_owner(self, db: Session, owner: str) -> List[Brand]:
        return db.query(Brand).filter(Brand.owner == owner).all()

    def search_by_name(self, db: Session, name: str) -> List[Brand]:
        return db.query(Brand).filter(Brand.name.ilike(f"%{name}%")).all()

    def exists_by_registration_number(
        self, db: Session, registration_number: str
    ) -> bool:
        return (
            db.query(Brand)
            .filter(Brand.registration_number == registration_number)
            .first()
            is not None
        )

    def update_status(
        self, db: Session, brand_id: int, status: BrandStatus
    ) -> Optional[Brand]:
        brand = self.get(db, brand_id)
        if brand:
            brand.status = status
            db.commit()
            db.refresh(brand)
        return brand

    def get_active_brands(self, db: Session) -> List[Brand]:
        return db.query(Brand).filter(Brand.status == BrandStatus.REGISTERED).all()
