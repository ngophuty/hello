from django.test import tag
from fastapi import FastAPI
from app.server.models import login


app =FastAPI()

username1 = login.database.username
password1 =login.database.password

@app.post("/login")

def logine(username : login.User):
    if username.username != username1 or username.password !=password1:
        return {"ban da nhap sai tai khoan hoac mat khau"}
    if username.username == username1 and username.password == password1:
        return {"dang nhap thanh cong"}