# 2 — Path Parameters

Reading dynamic values straight from the URL path.

## 2/a — Basic path parameter

```bash
cd example/2/a
uvicorn main:app --reload
```

| Route | Description |
|---|---|
| `GET /items/{item_id}` | `item_id: int` — non-integer values (e.g. `/items/foo`) return `422` |

`{item_id}` is a placeholder — replace it with a real number, don't paste
the braces literally:

```bash
curl http://127.0.0.1:8000/items/5
curl http://127.0.0.1:8000/items/foo   # 422, "foo" isn't an int
```

## 2/b — Fixed path before dynamic path

`/users/me` is declared *before* `/users/{user_id}` — if it were declared
after, `/users/{user_id}` would match `/users/me` first and treat `"me"`
as a `user_id`.

```bash
cd example/2/b
uvicorn main:app --reload
```

| Route | Description |
|---|---|
| `GET /users/me` | Returns `{"user_id": "the current user"}` |
| `GET /users/{user_id}` | Returns `{"user_id": <str>}` for any other value |

```bash
curl http://127.0.0.1:8000/users/me
curl http://127.0.0.1:8000/users/hero
```

## 2/c — Enum path parameter

Restricts a path parameter to a fixed set of values.

```bash
cd example/2/c
uvicorn main:app --reload
```

| Route | Description |
|---|---|
| `GET /models/{model_name}` | Only accepts `resnet` or `lenet`; anything else returns `422` |

```bash
curl http://127.0.0.1:8000/models/resnet
curl http://127.0.0.1:8000/models/bogus   # 422, not a valid enum value
```

Try any route at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
