from sqlalchemy import Column, Integer, String, Boolean, func, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(
        DateTime(timezone=True), server_default=func.current_timestamp(), nullable=False
    )
