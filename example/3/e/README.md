# 3/e — GET + POST, show / append / print specific

See [STEPS.md](STEPS.md) for a line-by-line walkthrough.

```bash
cd example/3/e
uvicorn main:app --reload
```

| Route | Description |
|---|---|
| `GET /items` | Shows all data (an in-memory list — resets on restart) |
| `POST /items` | Appends one item |
| `GET /items/{item_index}` | Prints one specific item by its position; out-of-range returns `404` |

```bash
curl -X POST http://127.0.0.1:8000/items -H "Content-Type: application/json" -d "{\"value\": \"first\"}"

curl http://127.0.0.1:8000/items
curl http://127.0.0.1:8000/items/0
```

**Postman:** three separate requests —

- `GET http://127.0.0.1:8000/items` — no body.
- `POST http://127.0.0.1:8000/items`, Body → raw → JSON: `{"value": "first"}`
- `GET http://127.0.0.1:8000/items/0` — no body.

Windows curl quoting, Postman basics, and "405 Method Not Allowed" are
covered generically in the [root README](../../../README.md).
