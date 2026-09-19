from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class CalculateRequest(BaseModel):
    a: float
    b: float
    # only these four words are accepted — anything else falls through
    # to the "else" branch below and returns an error.
    operation: str


@app.post("/calculate")
def calculate(request: CalculateRequest):
    if request.operation == "add":
        result = request.a + request.b
    elif request.operation == "subtract":
        result = request.a - request.b
    elif request.operation == "multiply":
        result = request.a * request.b
    elif request.operation == "divide":
        if request.b == 0:
            # Dividing by zero isn't a bug in the request's shape (that's
            # what a 422 is for) — it's a bad value. 400 is the right
            # status code for "the request was well-formed, but this
            # specific input can't be processed."
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        result = request.a / request.b
    else:
        raise HTTPException(
            status_code=400,
            detail="operation must be one of: add, subtract, multiply, divide",
        )

    return {"result": result}
