# 3/e — GET + POST, show / append / print specific, step by step

1. **Store data in a plain list**, outside any route function, so every
   request sees the same list: `data = []`.

2. **`GET /items` just returns it as-is** — showing all data.

3. **`POST /items` appends to it:**

   ```python
   @app.post("/items")
   def append_data(item: ItemRequest):
       data.append(item.value)
       return {"message": "Added", "data": data}
   ```

4. **`GET /items/{item_index}` reads one entry by its position**, with a
   manual bounds check before indexing into the list (Python would raise
   its own error for an out-of-range index, but a `404` is the correct
   HTTP response, not a `500`):

   ```python
   if item_index < 0 or item_index >= len(data):
       raise HTTPException(status_code=404, detail="Item not found")
   ```

This is the same shape as a real database — create, list, get-one —
just without anything surviving a restart.
