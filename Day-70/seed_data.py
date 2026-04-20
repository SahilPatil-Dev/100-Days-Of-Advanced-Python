import random
from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db.models import User, Order

db: Session = SessionLocal()

users = []
for i in range(10000):
    users.append(User(
        email=f"user{i}@example.com",
        age=random.randint(18, 60),
        created_at=datetime.now(timezone.utc) - timedelta(days=random.randint(0, 365)),
        extra_data={"source": "seed"} 
    ))

db.bulk_save_objects(users)
db.commit()

user_ids = [u[0] for u in db.query(User.id).all()]


orders = []
for i in range(50000):
    orders.append(Order(
        user_id=random.choice(user_ids),
        amount=round(random.uniform(100, 1000), 2),
        created_at=datetime.now(timezone.utc) - timedelta(days=random.randint(0, 365)),
        extra_data={"type": "random"}   
    ))

db.bulk_save_objects(orders)
db.commit()

db.close()

print("Seeding completed")