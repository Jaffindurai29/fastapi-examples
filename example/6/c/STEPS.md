# 6/c — PUT (MySQL), step by step

Same connection/table/seed boilerplate as [6/a](../a/STEPS.md). The
update itself:

```python
@app.put("/items/{item_id}")
def replace_item(item_id: int, item: ItemRequest, db: Session = Depends(get_db)):
    row = db.get(ItemModel, item_id)
    if row is None:
        raise HTTPException(status_code=404, detail="Item not found")
    row.value = item.value
    db.commit()
    db.refresh(row)
    return {"id": row.id, "value": row.value}
```

1. **Look the row up first** — `db.get(ItemModel, item_id)` returns
   `None` if that ID doesn't exist, so a clean `404` goes out instead of
   silently doing nothing.
2. **`row.value = item.value`** — this looks like a plain attribute
   assignment because it is one. SQLAlchemy's ORM tracks the change on
   `row` automatically; nothing needs to be re-added to the session.
3. **`db.commit()`** writes the change; **`db.refresh(row)`** makes sure
   `row` reflects exactly what's now in the database before it's
   returned.
