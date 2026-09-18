# 1 — First Steps

Writing and running your first FastAPI app.

## 1/a — Hello, FastAPI!

The simplest possible app: one route, no parameters.

```bash
cd example/1/a
uvicorn main:app --reload
```

| Route | Description |
|---|---|
| `GET /` | Returns `{"message": "Hello, FastAPI!"}` |

## 1/b — Path operations for other HTTP methods

A decorator per HTTP method (`GET`, `POST`, `PUT`, `DELETE`), each doing
something real against an in-memory list.

```bash
cd example/1/b
uvicorn main:app --reload
```

| Route | Description |
|---|---|
| `GET /items` | Lists all items |
| `POST /items?name=` | Appends an item |
| `PUT /items/{item_id}?name=` | Replaces the item at index `item_id` |
| `DELETE /items/{item_id}` | Removes the item at index `item_id` |

`{item_id}` is a placeholder — replace it with a real number (e.g. `0`),
don't paste the braces literally. Try it:

```bash
curl -X POST "http://127.0.0.1:8000/items?name=Baz"
curl -X PUT "http://127.0.0.1:8000/items/0?name=Qux"
curl -X DELETE "http://127.0.0.1:8000/items/0"
```

Or use [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs), which
fills in path/query values through a form instead of a raw URL.
