# 6 — Interactive Docs

Every FastAPI app gets a live Swagger UI (`/docs`) and ReDoc page
(`/redoc`) for free, generated from an OpenAPI schema built out of your
type hints, `response_model`s, and docstrings.

## 6/a — Improving the docs with docstrings and metadata

```bash
cd example/6/a
uvicorn main:app --reload
```

| Route | Description |
|---|---|
| `GET /items/{item_id}` | Same as a basic path parameter, but with a `summary` and a docstring that both show up in `/docs` |

Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) and
[http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) to see the
difference the summary/docstring makes, and
[http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)
for the raw schema both pages are built from.
