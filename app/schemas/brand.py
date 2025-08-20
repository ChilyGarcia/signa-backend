from app.models.brand import BrandStatus
from pydantic import BaseModel


class BrandBase(BaseModel):
    name: str
    description: str | None = None
    owner: str
    registration_number: str | None = None


class BrandCreate(BrandBase):
    pass


class BrandUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    owner: str | None = None
    registration_number: str | None = None
    status: BrandStatus | None = None


class Brand(BrandBase):
    id: int
    status: BrandStatus

    class Config:
        from_attributes = True
