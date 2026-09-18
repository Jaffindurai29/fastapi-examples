from fastapi import FastAPI

app = FastAPI()

fake_items = [{"name": "Foo"}, {"name": "Bar"}]

@app.get("/items")
def list_items():
    return fake_items

@app.post("/items")
def create_item(name: str):
    fake_items.append({"name": name})
    return fake_items[-1]

@app.put("/items/{item_id}")
def replace_item(item_id: int, name: str):
    fake_items[item_id] = {"name": name}
    return fake_items[item_id]

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return fake_items.pop(item_id)
