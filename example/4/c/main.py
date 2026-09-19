from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

data = ["first", "second"]


class ItemRequest(BaseModel):
    value: str


# PUT replaces the item at this index entirely — the client must send
# the full value, even if only part of it actually changed.
@app.put("/items/{item_index}")
def replace_item(item_index: int, item: ItemRequest):
    if item_index < 0 or item_index >= len(data):
        raise HTTPException(status_code=404, detail="Item not found")
    data[item_index] = item.value
    return {"index": item_index, "value": data[item_index]}
