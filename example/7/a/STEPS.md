# 7/a — MySQL backend, full CRUD + CORS, step by step

This file is [topic 6](../../6)'s five routes (6/a=GET, 6/b=POST,
6/c=PUT, 6/d=PATCH, 6/e=DELETE) combined into one running app, plus
CORS — the same relationship [5/a](../../5/a) has to
[topic 4](../../4). If you've already read topic 6's STEPS.md files,
nothing about the database logic itself is new here; this walks through
what's added on top.

1. **Same connection, table, and seed boilerplate as every topic 6
   page** — `DATABASE_URL` from environment variables, `ItemModel` as
   the table, seeding two rows if the table is empty. Only the table
   name differs (`crud_react_items`, so this topic's demo data doesn't
   collide with topic 6's).

2. **All five route functions, unchanged from topic 6**, just declared
   on the same `app` instead of five separate ones:

   ```python
   @app.get("/items")
   def list_items(db: Session = Depends(get_db)): ...

   @app.get("/items/{item_id}")
   def get_item(item_id: int, db: Session = Depends(get_db)): ...

   @app.post("/items", status_code=status.HTTP_201_CREATED)
   def create_item(item: ItemRequest, db: Session = Depends(get_db)): ...

   @app.put("/items/{item_id}")
   def replace_item(item_id: int, item: ItemRequest, db: Session = Depends(get_db)): ...

   @app.patch("/items/{item_id}")
   def update_item(item_id: int, patch: ItemPatch, db: Session = Depends(get_db)): ...

   @app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
   def delete_item(item_id: int, db: Session = Depends(get_db)): ...
   ```

   **Why combine them:** a real frontend needs to `GET`, `POST`, `PUT`,
   `PATCH`, and `DELETE` against the *same* running server — five
   separate standalone apps on five different ports wouldn't let one
   React page talk to all of them at once.

3. **The one genuinely new piece: CORS**, imported and registered once,
   right after creating `app` — identical to
   [5/a's STEPS.md](../../5/a/STEPS.md), just added to the MySQL-backed
   app instead of the array-backed one:

   ```python
   from fastapi.middleware.cors import CORSMiddleware

   app.add_middleware(
       CORSMiddleware,
       allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
   )
   ```

4. **Difference from 5/a that matters for the frontend:** every
   response here includes a real database `id`
   (`{"id": 1, "value": "first"}`), not an array position
   (`{"index": 0, "value": "first"}`). That's why
   [7/react](../react) addresses rows by `id` — see its
   [STEPS.md](../react/STEPS.md) for exactly what that changes on the
   frontend side.
