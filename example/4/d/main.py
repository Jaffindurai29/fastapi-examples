from typing import Optional

from fastapi import FastAPI, HTTPException

app = FastAPI()

data = ["first", "second"]


@app.get("/items")
def list_items():
    return data


# Optional, unlike PUT's `value` — PATCH lets the client send only the
# fields it actually wants to change.
@app.patch("/items/{item_index}")
def update_item(item_index: int, value: Optional[str] = None):
    if item_index < 0 or item_index >= len(data):
        raise HTTPException(status_code=404, detail="Item not found")
    if value is not None:
        data[item_index] = value
    return {"index": item_index, "value": data[item_index]}
