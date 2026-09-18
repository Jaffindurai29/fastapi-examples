from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.post("/items")
def create_item(item: Item):
    item_dict = item.dict()
    if item.tax is not None:
        item_dict["price_with_tax"] = item.price + item.tax
    return item_dict
