from sqlalchemy import Column, Integer, String, Float, Boolean
from app.db.base_class import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    is_active = Column(Boolean, default=False)
