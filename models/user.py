from pydantic import BaseModel



class UserModel(BaseModel):
    id: int
    name: str
    email: str
    age: int


class User:
    
    def __init__(self):
        self.users = [
            {"id": 1, "name": "John Doe", "email": "john.doe@example.com", "age": 28},
            {"id": 2, "name": "Jane Smith", "email": "jane.smith@example.com", "age": 35},
            {"id": 3, "name": "Bob Johnson", "email": "bob.johnson@example.com", "age": 42},
        ]

    def get_all_users(self):
        return self.users
    
    def get_user_by_id(self, user_id : int):
        for user in self.users:
            if user["id"] == user_id:
                return user
        return None
    
    def create_user(self, user : UserModel):
        self.users.append(user.dict())
        return user
    
    def update_user(self, user_id, user : UserModel):
        users = self.users
        for i in range(len(users)):
            if users[i]["id"] == user_id:
                users[i] = user.dict()
                return user
        return None
    
    def delete_user(self, user_id : int):
        users = self.users
        for i in range(len(users)):
            if users[i]["id"] == user_id:
                del users[i]
                return True
        return False



