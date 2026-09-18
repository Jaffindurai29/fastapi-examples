# 4 — Request Body

Accepting structured JSON data using Pydantic models.

## 4/a — Defining a data shape with Pydantic

```bash
cd example/4/a
uvicorn main:app --reload
```

| Route | Description |
|---|---|
| `POST /items` (JSON body: `name`, `price`, optional `description`/`tax`) | Echoes back the parsed `Item` |

```bash
curl -X POST http://127.0.0.1:8000/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Foo", "price": 10.5}'
```

## 4/b — Using the parsed model

```bash
cd example/4/b
uvicorn main:app --reload
```

| Route | Description |
|---|---|
| `POST /items` | Same body as 4/a, plus computes `price_with_tax` when `tax` is set |

```bash
curl -X POST http://127.0.0.1:8000/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Foo", "price": 10.5, "tax": 1.5}'
```

## 4/c — Body, path, and query together

```bash
cd example/4/c
uvicorn main:app --reload
```

| Route | Description |
|---|---|
| `PUT /items/{item_id}?q=` | Path param (`item_id`), optional query param (`q`), and a JSON body (`item`) all in one function |

`{item_id}` is a placeholder — replace it with a real number, don't paste
the braces literally:

```bash
curl -X PUT "http://127.0.0.1:8000/items/3?q=hi" \
  -H "Content-Type: application/json" \
  -d '{"name": "Foo", "price": 10.5}'
```

Try any route at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
— use "Try it out" to send a JSON body from the browser.
