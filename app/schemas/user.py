from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    password: str
    is_active: bool


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        from_attributes = True
