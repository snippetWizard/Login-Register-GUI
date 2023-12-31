import sqlalchemy
from sqlalchemy import Column, Text, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """User account."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    username = Column(String(255), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    first_name = Column(String(255))
    last_name = Column(String(255))
    bio = Column(Text)
    avatar_url = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())

