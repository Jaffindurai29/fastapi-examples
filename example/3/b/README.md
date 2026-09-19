# 3/b — POST, dynamic name

See [STEPS.md](STEPS.md) for a line-by-line walkthrough.

```bash
cd example/3/b
uvicorn main:app --reload
```

| Route | Description |
|---|---|
| `POST /hello` | Same greeting as 3/a, but the name comes from a JSON body |

```bash
curl -X POST http://127.0.0.1:8000/hello -H "Content-Type: application/json" -d "{\"name\": \"Alice\"}"
```

**Postman:** Method `POST`, URL `http://127.0.0.1:8000/hello`, Body →
raw → JSON:

```json
{"name": "Alice"}
```

Windows curl quoting, Postman basics, and "405 Method Not Allowed" are
covered generically in the [root README](../../../README.md).
