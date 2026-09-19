from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class AddRequest(BaseModel):
    a: float
    b: float


@app.post("/add")
def add_numbers(request: AddRequest):
    return {"result": request.a + request.b}
