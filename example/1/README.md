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
| `POST /items?name=Baz` | Appends an item |
| `PUT /items/{item_id}?name=Qux` | Replaces an item |
| `DELETE /items/{item_id}` | Removes an item |

Try any route at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
