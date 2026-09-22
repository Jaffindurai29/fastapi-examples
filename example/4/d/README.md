# 4/d — PATCH

Partially updating the item at a given index — the field is optional.
See [STEPS.md](STEPS.md) for a line-by-line walkthrough.

```bash
cd example/4/d
uvicorn main:app --reload
```

| Route | Description |
|---|---|
| `GET /items` | Returns the current list |
| `PATCH /items/{item_index}` | Updates `value` only if it's sent (query parameter); out-of-range returns `404` |

```bash
curl -X PATCH "http://127.0.0.1:8000/items/1?value=patched"

curl -X PATCH http://127.0.0.1:8000/items/0
```

**Postman:** Method `PATCH`, URL `http://127.0.0.1:8000/items/1`, Params →
`value` = `patched`.

Try the request with no `value` param too — the item at that index
comes back unchanged, since nothing was sent to update.

Windows curl quoting, Postman basics, and "405 Method Not Allowed" are
covered generically in the [root README](../../../README.md).
