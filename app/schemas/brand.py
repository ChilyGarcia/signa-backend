from app.models.brand import BrandStatus
from pydantic import BaseModel


class BrandBase(BaseModel):
    name: str
    description: str | None = None
    owner: str
    registration_number: str | None = None


class BrandCreate(BrandBase):
    created_by: int | None = None


class BrandUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    owner: str | None = None
    registration_number: str | None = None
    status: BrandStatus | None = None


class UserInfo(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: str

    class Config:
        from_attributes = True


class Brand(BrandBase):
    id: int
    status: BrandStatus
    created_by: int
    creator: UserInfo | None = None

    class Config:
        from_attributes = True
