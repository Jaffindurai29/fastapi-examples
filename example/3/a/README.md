# 3/a — GET, dynamic name

See [STEPS.md](STEPS.md) for a line-by-line walkthrough.

```bash
cd example/3/a
uvicorn main:app --reload
```

| Route | Description |
|---|---|
| `GET /hello/{name}` | Returns a greeting built from whatever name is in the URL |

```bash
curl http://127.0.0.1:8000/hello/Alice
```

**Postman:** Method `GET`, URL `http://127.0.0.1:8000/hello/Alice` — no
Headers or Body needed.

Windows curl quoting, Postman basics, and "405 Method Not Allowed" are
covered generically in the [root README](../../../README.md).
