# 3/d — POST, calculator

See [STEPS.md](STEPS.md) for a line-by-line walkthrough.

```bash
cd example/3/d
uvicorn main:app --reload
```

| Route | Description |
|---|---|
| `POST /calculate` | `operation` is one of `add`, `subtract`, `multiply`, `divide`; dividing by zero returns `400` instead of crashing |

```bash
curl -X POST http://127.0.0.1:8000/calculate -H "Content-Type: application/json" -d "{\"a\": 5, \"b\": 3, \"operation\": \"multiply\"}"

curl -i -X POST http://127.0.0.1:8000/calculate -H "Content-Type: application/json" -d "{\"a\": 5, \"b\": 0, \"operation\": \"divide\"}"   # 400
```

**Postman:** Method `POST`, URL `http://127.0.0.1:8000/calculate`, Body
→ raw → JSON:

```json
{"a": 5, "b": 3, "operation": "multiply"}
```

Try `{"a": 5, "b": 0, "operation": "divide"}` to see the `400` error
response instead of a crash.

Windows curl quoting, Postman basics, and "405 Method Not Allowed" are
covered generically in the [root README](../../../README.md).
