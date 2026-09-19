# 4/b — POST

Adding a new item to the end of the array. Seeded with two items so
you can see the new one land after them. See [STEPS.md](STEPS.md) for a
line-by-line walkthrough.

```bash
cd example/4/b
uvicorn main:app --reload
```

| Route | Description |
|---|---|
| `POST /items` | Appends one value; returns `201 Created` with the new item's index |

```bash
curl -i -X POST http://127.0.0.1:8000/items -H "Content-Type: application/json" -d "{\"value\": \"third\"}"
```

**Postman:** Method `POST`, URL `http://127.0.0.1:8000/items`, Body →
raw → JSON:

```json
{"value": "third"}
```

Expected response: `201 Created`, `{"index": 2, "value": "third"}`.

Windows curl quoting, Postman basics, and "405 Method Not Allowed" are
covered generically in the [root README](../../../README.md).
