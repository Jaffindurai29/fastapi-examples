from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

data = ["first", "second"]


# Optional, unlike PUT's ItemRequest — PATCH lets the client send only
# the fields it actually wants to change.
class ItemPatch(BaseModel):
    value: Optional[str] = None


@app.patch("/items/{item_index}")
def update_item(item_index: int, patch: ItemPatch):
    if item_index < 0 or item_index >= len(data):
        raise HTTPException(status_code=404, detail="Item not found")
    if patch.value is not None:
        data[item_index] = patch.value
    return {"index": item_index, "value": data[item_index]}
