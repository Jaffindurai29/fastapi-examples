# 3/c — POST, add two numbers

See [STEPS.md](STEPS.md) for a line-by-line walkthrough.

```bash
cd example/3/c
uvicorn main:app --reload
```

| Route | Description |
|---|---|
| `POST /add` | Returns `{"result": a + b}` |

```bash
curl -X POST http://127.0.0.1:8000/add -H "Content-Type: application/json" -d "{\"a\": 5, \"b\": 3}"
```

**Postman:** Method `POST`, URL `http://127.0.0.1:8000/add`, Body → raw
→ JSON:

```json
{"a": 5, "b": 3}
```

Expected response: `{"result": 8.0}`

Windows curl quoting, Postman basics, and "405 Method Not Allowed" are
covered generically in the [root README](../../../README.md).
