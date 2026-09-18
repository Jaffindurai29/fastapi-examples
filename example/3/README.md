# 3 — Query Parameters

Reading optional values from the query string.

## 3/a — Basic query parameters

```bash
cd example/3/a
uvicorn main:app --reload
```

| Route | Description |
|---|---|
| `GET /items?skip=0&limit=10` | Slices an in-memory list; both params default if omitted |

## 3/b — Optional query parameter

```bash
cd example/3/b
uvicorn main:app --reload
```

| Route | Description |
|---|---|
| `GET /items/{item_id}?q=` | `q` is optional; included in the response only if given |

## 3/c — Required query parameter

A query parameter with no default value is required, even though it's
not part of the path.

```bash
cd example/3/c
uvicorn main:app --reload
```

| Route | Description |
|---|---|
| `GET /items/{item_id}?needy=` | `needy` is required — omitting it returns `422` |

## 3/d — Mixing path and query parameters

```bash
cd example/3/d
uvicorn main:app --reload
```

| Route | Description |
|---|---|
| `GET /users/{user_id}/items/{item_id}?q=&short=` | Two path params plus an optional `q` and a `bool` `short` flag |

Try any route at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
