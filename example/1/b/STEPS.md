# 1/b — Other HTTP methods, step by step

Same idea as [1/a](../a/STEPS.md), repeated for every HTTP verb:

```python
@app.get("/items")      # read
def list_items(): ...

@app.post("/items")     # create
def create_item(name: str): ...

@app.put("/items/{item_id}")    # replace
def replace_item(item_id: int, name: str): ...

@app.delete("/items/{item_id}") # remove
def delete_item(item_id: int): ...
```

The decorator you choose (`@app.get`, `@app.post`, `@app.put`,
`@app.delete`) is the only thing that changes — everything else about
writing the function is the same as 1/a. `GET` reads data, `POST`
creates it, `PUT` replaces it, `DELETE` removes it.
