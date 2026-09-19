# 6/d — PATCH (MySQL), step by step

Same connection/table/seed boilerplate as [6/a](../a/STEPS.md). Same
"required vs. optional" distinction as the [array topic's PATCH](../../4/d/STEPS.md):

```python
class ItemPatch(BaseModel):
    value: Optional[str] = None

@app.patch("/items/{item_id}")
def update_item(item_id: int, patch: ItemPatch, db: Session = Depends(get_db)):
    row = db.get(ItemModel, item_id)
    if row is None:
        raise HTTPException(status_code=404, detail="Item not found")
    if patch.value is not None:
        row.value = patch.value
    db.commit()
    db.refresh(row)
    return {"id": row.id, "value": row.value}
```

1. **`ItemPatch.value` is optional** — unlike [6/c](../c/STEPS.md)'s
   `ItemRequest`, where `value` is required.
2. **`if patch.value is not None: row.value = patch.value`** — only
   updates the row if the client actually sent a value; an empty body
   (`{}`) leaves it untouched.
