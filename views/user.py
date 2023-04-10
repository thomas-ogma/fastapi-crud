from models.user import User, UserModel

user = User()

def create_user(userModal: UserModel):
    return user.create_user(userModal)


def read_users():
    return user.get_all_users()

def read_user(user_id: int):
    user_data = user.get_user_by_id(user_id)
    if user_data:
        return user_data
    else:
        return {"error": "User not Found"}


def update_user(user_id: int, userModal: UserModel):
    updated_user = user.update_user(user_id, userModal)
    if updated_user:
        return updated_user
    else:
        return {"error": "User not found"}

def delete_user(user_id: int):
    if user.delete_user(user_id):
        return {"message": "User deleted successfully"}
    else:
        return {"error": "User not found"}


