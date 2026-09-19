from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Same idea as exercise 1, but the name now comes from a JSON body
# instead of the URL — that's the difference between GET and POST here.
class NameRequest(BaseModel):
    name: str


@app.post("/hello")
def say_hello(request: NameRequest):
    return {"message": f"Hello, {request.name}!"}
