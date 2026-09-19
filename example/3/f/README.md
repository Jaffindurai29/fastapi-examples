# 3/f — POST, login authentication

See [STEPS.md](STEPS.md) for a line-by-line walkthrough.

```bash
cd example/3/f
uvicorn main:app --reload
```

| Route | Description |
|---|---|
| `POST /login` | Checks username/password against a hardcoded dict; `401` on any mismatch, without revealing whether the username or the password was wrong |

```bash
curl -i -X POST http://127.0.0.1:8000/login -H "Content-Type: application/json" -d "{\"username\": \"admin\", \"password\": \"password123\"}"

curl -i -X POST http://127.0.0.1:8000/login -H "Content-Type: application/json" -d "{\"username\": \"admin\", \"password\": \"wrong\"}"   # 401
```

**Postman:** Method `POST`, URL `http://127.0.0.1:8000/login`, Body →
raw → JSON:

```json
{"username": "admin", "password": "password123"}
```

Change `password` to anything else (or `username` to anything not in
the hardcoded dict) to see the `401` response.

This one is deliberately the simplest possible version — plain-text
password comparison, no tokens. Real login systems hash passwords before
storing them and issue a token (e.g. JWT) on success instead of just a
message; that's a natural next topic once this shape feels comfortable.

Windows curl quoting, Postman basics, and "405 Method Not Allowed" are
covered generically in the [root README](../../../README.md).
