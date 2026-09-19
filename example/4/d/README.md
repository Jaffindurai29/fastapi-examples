# 4/d — PATCH

Partially updating the item at a given index — the field is optional.
See [STEPS.md](STEPS.md) for a line-by-line walkthrough.

```bash
cd example/4/d
uvicorn main:app --reload
```

| Route | Description |
|---|---|
| `PATCH /items/{item_index}` | Updates `value` only if it's sent; out-of-range returns `404` |

```bash
curl -X PATCH http://127.0.0.1:8000/items/1 -H "Content-Type: application/json" -d "{\"value\": \"patched\"}"

curl -X PATCH http://127.0.0.1:8000/items/0 -H "Content-Type: application/json" -d "{}"
```

**Postman:** Method `PATCH`, URL `http://127.0.0.1:8000/items/1`, Body →
raw → JSON:

```json
{"value": "patched"}
```

Try an empty body (`{}`) too — the item at that index comes back
unchanged, since nothing was sent to update.

Windows curl quoting, Postman basics, and "405 Method Not Allowed" are
covered generically in the [root README](../../../README.md).
