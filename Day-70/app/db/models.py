from sqlalchemy import (
    Column, Integer, String, Float, DateTime,
    ForeignKey, Index, CheckConstraint, func
)
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.dialects.postgresql import JSONB

Base = declarative_base()


class User(Base):
    __tablename__ = "users"  

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True, nullable=False)
    age = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index = True)
    extra_data = Column(JSONB, nullable=True)

    orders = relationship("Order", back_populates="user")

    __table_args__ = ( 
        Index("idx_user_age_created", "age", "created_at"),
        CheckConstraint("age >= 18", name="check_user_age"),
    )


class Order(Base):
    __tablename__ = "orders" 

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    amount = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index = True)
    extra_data = Column(JSONB, nullable=True)

    user = relationship("User", back_populates="orders")

    __table_args__ = (  
        CheckConstraint("amount > 0", name="check_order_amount"),
    )