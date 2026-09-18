from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: str, needy: str):
    return {"item_id": item_id, "needy": needy}
