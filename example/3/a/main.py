from fastapi import FastAPI

app = FastAPI()

fake_items = [{"name": "Foo"}, {"name": "Bar"}, {"name": "Baz"}]

@app.get("/items")
def list_items(skip: int = 0, limit: int = 10):
    return fake_items[skip : skip + limit]
