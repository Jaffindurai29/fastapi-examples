from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Data lives in a plain Python list while the server is running. It
# resets every time you restart the app — see the Databases topic
# (example/8) for how to make it survive restarts.
data = []


class ItemRequest(BaseModel):
    value: str


# Show all data.
@app.get("/items")
def show_data():
    return data


# Append data — adds one new item to the end of the list.
@app.post("/items")
def append_data(item: ItemRequest):
    data.append(item.value)
    return {"message": "Added", "data": data}


# Print specific data — one item, found by its position in the list.
@app.get("/items/{item_index}")
def get_specific_data(item_index: int):
    if item_index < 0 or item_index >= len(data):
        raise HTTPException(status_code=404, detail="Item not found")
    return {"index": item_index, "value": data[item_index]}
