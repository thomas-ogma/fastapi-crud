from fastapi import FastAPI
from pydantic import BaseModel 

app = FastAPI()

# Define the data model for our API using Pydantic:
class User(BaseModel):
    id: int
    name: str
    email: str
    age: int

# defining constant for error message
error = "User not found"

# Create a list of users to serve as our database 
users = [
    {"id": 1, "name": "John Doe", "email": "john.doe@example.com", "age": 28},
    {"id": 2, "name": "Jane Smith", "email": "jane.smith@example.com", "age": 35},
    {"id": 3, "name": "Bob Johnson", "email": "bob.johnson@example.com", "age": 42},
]


# CREATE API
@app.post("/users")
def create_user(user: User):
    users.append(user.dict())
    return user

# READ APIs
@app.get("/users")
def read_users():
    return users

@app.get("/users/{user_id}")
def read_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    return {"error": {error}}


# UPDATE API
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    for i in range(len(users)):
        if users[i]["id"] == user_id:
            users[i] = user.dict()
            return user
    return {"error": {error}}


# DELETE API
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for i in range(len(users)):
        if users[i]["id"] == user_id:
            del users[i]
            return {"message": "User deleted successfully"}
    return {"error": {error}}




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)



