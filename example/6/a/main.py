from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}", summary="Get one item")
def read_item(item_id: int):
    """
    Fetch a single item by its ID.

    - **item_id**: the numeric ID of the item to look up.
    """
    return {"item_id": item_id}
