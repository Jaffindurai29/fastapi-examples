from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

data = ["first", "second"]


class ItemRequest(BaseModel):
    value: str


# Add a new item to the end of the array.
@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: ItemRequest):
    data.append(item.value)
    return {"index": len(data) - 1, "value": item.value}
