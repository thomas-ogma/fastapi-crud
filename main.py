from fastapi import FastAPI
from pydantic import BaseModel
from views.user import *

app = FastAPI()


# Defining Routes

# CREATE API
app.post("/users")(create_user)


# READ APIs
app.get("/users")(read_users)
app.get("/users/{user_id}")(read_user)


# UPDATE API
app.put("/users/{user_id}")(update_user)


# DELETE API
app.delete("/users/{user_id}")(delete_user)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)



