from app.schemas.user import UserCreate

# In-memory storage (for now)
users_db = []
user_id_counter = 1


def create_user(user: UserCreate):

    global user_id_counter

    new_user = {
        "id": user_id_counter,
        "email": user.email,
        "age": user.age
    }

    users_db.append(new_user)
    user_id_counter += 1

    return new_user


def get_users():
    return users_db