from app.models.brand import BrandStatus
from pydantic import BaseModel


class BrandBase(BaseModel):
    name: str
    description: str | None = None
    owner: str
    registration_number: str | None = None
    status: BrandStatus


class BrandCreate(BrandBase):
    pass


class Brand(BrandBase):
    id: int
    status: BrandStatus

    class Config:
        from_attributes = True
