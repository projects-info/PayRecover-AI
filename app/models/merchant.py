from sqlalchemy import Column, Integer, String
from app.models.base import Base


class Merchant(Base):
    __tablename__ = "merchants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    industry = Column(String)
    email = Column(String, unique=True)