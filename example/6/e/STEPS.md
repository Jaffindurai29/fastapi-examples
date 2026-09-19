# 6/e — DELETE (MySQL), step by step

Same connection/table/seed boilerplate as [6/a](../a/STEPS.md). The
delete itself:

```python
@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    row = db.get(ItemModel, item_id)
    if row is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(row)
    db.commit()
```

1. **Look the row up first** — same `404`-if-missing pattern as every
   other route in this topic.
2. **`db.delete(row)` then `db.commit()`** — stages the deletion, then
   writes it.
3. **Unlike the array topic**, deleting a row here never shifts any
   other row's `id` — MySQL's auto-increment `id` is a stable identity,
   not a position in a list. That's one of the real advantages of a
   database over an in-memory array for anything that needs to survive
   deletions predictably.
