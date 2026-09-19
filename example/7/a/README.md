# 7/a — MySQL backend, full CRUD + CORS

All five verbs from [topic 6](../../6) combined into one running app,
plus `CORSMiddleware` so the [React frontend](../react) can call it.
Same [setup](../../6/a/README.md#setup) as topic 6 — install
`sqlalchemy`/`pymysql`, create the database, set your connection env
vars (or point `DATABASE_URL` at SQLite for a quick local try).

```bash
cd example/7/a
uvicorn main:app --reload
```

| Route | Description |
|---|---|
| `GET /items` | Every row (seeded with two on first run) |
| `GET /items/{item_id}` | One row by its database ID; `404` if missing |
| `POST /items` | Insert a new row; `201 Created` |
| `PUT /items/{item_id}` | Replace a row's value entirely; `404` if missing |
| `PATCH /items/{item_id}` | Partially update a row (field optional); `404` if missing |
| `DELETE /items/{item_id}` | Remove a row; `204 No Content`; `404` if missing |

```bash
curl http://127.0.0.1:8000/items
curl -X POST http://127.0.0.1:8000/items -H "Content-Type: application/json" -d "{\"value\": \"third\"}"
curl -X PUT http://127.0.0.1:8000/items/1 -H "Content-Type: application/json" -d "{\"value\": \"replaced\"}"
curl -X PATCH http://127.0.0.1:8000/items/2 -H "Content-Type: application/json" -d "{\"value\": \"patched\"}"
curl -i -X DELETE http://127.0.0.1:8000/items/3
```

**Postman:** same five requests as [topic 6](../../6) — Method +
`http://127.0.0.1:8000/items` (with `/{id}` where needed), Body → raw →
JSON where a body is needed.

Windows curl quoting, Postman basics, and "405 Method Not Allowed" are
covered generically in the [root README](../../../README.md).
