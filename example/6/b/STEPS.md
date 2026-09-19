# 6/b — POST (MySQL), step by step

Same connection/table/seed boilerplate as [6/a](../a/STEPS.md). What's
new here is the insert itself:

```python
@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: ItemRequest, db: Session = Depends(get_db)):
    row = ItemModel(value=item.value)
    db.add(row)
    db.commit()
    db.refresh(row)
    return {"id": row.id, "value": row.value}
```

1. **`ItemModel(value=item.value)`** — builds a new ORM object in
   memory; nothing is written to the database yet.
2. **`db.add(row)`** — stages it for insertion.
3. **`db.commit()`** — actually writes it, and this is the point where
   MySQL assigns the real auto-incrementing `id`.
4. **`db.refresh(row)`** — pulls that generated `id` back into `row`
   from the database, so the function can return it. Without this
   step, `row.id` would still be `None`.
