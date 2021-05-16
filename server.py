from typing import Optional

from fastapi import FastAPI, Form, Cookie
from fastapi.responses import Response

app = FastAPI()

users = {
    "shaggy@user.com": {
        "name": "Ruslan",
        "password": "ruslan123",
        "balance": 100_000,
    },
    "petr@user.com": {
        "name": "Petr",
        "password": "petr123",
        "balance": 50_000,
    },
}


@app.get("/")
def index_page(username: Optional[str] = Cookie(default=None)):
    with open("templates/index.html", 'r') as f:
        login_page = f.read()
    if username:
        return Response(f"Привеет, {users[username]['name']}!", media_type='text/html')
    else:
        return Response(login_page, media_type="text/html")

@app.post("/login")
def login_page(username : str = Form(...), password : str = Form(...)):

    user = users.get(username)
    if not user or user['password'] != password:
        return Response("Я вас не знаю!", media_type="text/html")
    else:
        response = Response(
            f"Привееет, {user['name']}!<br>Баланс: {user['balance']}",
            media_type="text/html")
        response.set_cookie(key="username", value=username)
        return response