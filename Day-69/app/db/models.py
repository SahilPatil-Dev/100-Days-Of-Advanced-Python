from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey,
    Index,
    CheckConstraint,
    func,
    JSON
)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True, index=True, nullable=False)
    age = Column(Integer, nullable=False)

    created_at = Column(DateTime, server_default=func.now(), index=True)
    
    password_hash = Column(String, nullable=False)
    
    role = Column(String, default="user")

    orders = relationship("Order", back_populates="user", cascade="all, delete-orphan")

    __table_args__ = (
        Index("idx_user_age_created", "age", "created_at"),
        CheckConstraint("age >= 18", name="check_user_age"),
    )


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"), index=True, nullable=False)
    amount = Column(Float, nullable=False)

    created_at = Column(DateTime, server_default=func.now())

    extra_data = Column(
        JSON().with_variant(JSONB, "postgresql"),
        nullable=False,
        default=dict
    )

    user = relationship("User", back_populates="orders")

    __table_args__ = (
        CheckConstraint("amount > 0", name="check_order_amount"),
    )