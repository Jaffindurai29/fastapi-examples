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

```bash
curl "http://127.0.0.1:8000/items?skip=1&limit=2"
```

## 3/b — Optional query parameter

```bash
cd example/3/b
uvicorn main:app --reload
```

| Route | Description |
|---|---|
| `GET /items/{item_id}?q=` | `q` is optional; included in the response only if given |

`{item_id}` is a placeholder — replace it with a real value, don't paste
the braces literally:

```bash
curl http://127.0.0.1:8000/items/5
curl "http://127.0.0.1:8000/items/5?q=hi"
```

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

```bash
curl http://127.0.0.1:8000/items/5             # 422, "needy" is missing
curl "http://127.0.0.1:8000/items/5?needy=x"
```

## 3/d — Mixing path and query parameters

```bash
cd example/3/d
uvicorn main:app --reload
```

| Route | Description |
|---|---|
| `GET /users/{user_id}/items/{item_id}?q=&short=` | Two path params plus an optional `q` and a `bool` `short` flag |

`{user_id}` and `{item_id}` are placeholders in the route pattern above —
they're not meant to be pasted literally into a URL. A real request looks
like:

```bash
curl "http://127.0.0.1:8000/users/1/items/foo?q=hi&short=true"
```

(`short` accepts `true`/`false`, `1`/`0`, or `yes`/`no` — not the word
`bool`.)

Try any route at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs),
which fills in path/query values through a form instead of a raw URL.
