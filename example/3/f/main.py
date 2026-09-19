from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# A stand-in for a users table. Real apps never store plain-text
# passwords like this — passwords are hashed before saving, and
# compared as hashes, never as plain text. Keeping this basic version
# plain-text is just to show the shape of a login check clearly.
fake_users_db = {
    "admin": "password123",
}


class LoginRequest(BaseModel):
    username: str
    password: str


@app.post("/login")
def login(request: LoginRequest):
    correct_password = fake_users_db.get(request.username)

    if correct_password is None or correct_password != request.password:
        # Don't say *which* part was wrong (unknown username vs. wrong
        # password) — that tells an attacker whether a username exists.
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {"message": f"Welcome, {request.username}!"}
