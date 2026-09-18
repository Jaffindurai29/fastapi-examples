# 5 — Response & Status Codes

Controlling response shape, status codes, and error handling.

## 5/a — Setting a status code

```bash
cd example/5/a
uvicorn main:app --reload
```

| Route | Description |
|---|---|
| `POST /items?name=` | Returns `201 Created` instead of the default `200` |

```bash
curl -i -X POST "http://127.0.0.1:8000/items?name=Foo"
```

## 5/b — Restricting the response shape with `response_model`

`UserIn` accepts a `password`, but `response_model=UserOut` filters it out
of the response — the password never leaves the server.

```bash
cd example/5/b
uvicorn main:app --reload
```

| Route | Description |
|---|---|
| `POST /users` (JSON body: `username`, `password`, `email`) | Response includes only `username` and `email` |

```bash
curl -X POST http://127.0.0.1:8000/users \
  -H "Content-Type: application/json" \
  -d '{"username": "bob", "password": "secret", "email": "bob@example.com"}'
```

## 5/c — Raising errors with `HTTPException`

```bash
cd example/5/c
uvicorn main:app --reload
```

| Route | Description |
|---|---|
| `GET /items/foo` | Returns `{"item": "The Foo Wrestlers"}` |
| `GET /items/anything-else` | Returns `404` with `{"detail": "Item not found"}` |

```bash
curl http://127.0.0.1:8000/items/foo
curl -i http://127.0.0.1:8000/items/bar   # 404
```

Try any route at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
