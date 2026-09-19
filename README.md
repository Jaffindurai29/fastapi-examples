# fast-api-learn

Learning workspace for [FastAPI](https://fastapi.tiangolo.com/), with small
example apps under `example/` and a bilingual (English + Tanglish) Fumadocs
documentation site under `fastapi/`.

## Project layout

```
fast-api-learn/
├── example/           # one folder per topic, lettered subfolders per snippet
│   ├── 1/a            # GET
│   ├── 2/a, 2/b       # Path Parameters
│   ├── 3/a            # POST
│   ├── 4/a..4/e       # Array + CRUD (GET/POST/PUT/PATCH/DELETE)
│   ├── 5/a, 5/react   # React + Array + CRUD (array backend + frontend)
│   ├── 6/a..6/e       # MySQL + CRUD
│   └── 7/a, 7/react   # React + MySQL + CRUD (MySQL backend + frontend)
│   (see example/README.md for the full index,
│    and each letter folder's own STEPS.md for a code walkthrough)
├── fastapi/           # Fumadocs docs site (Next.js) — see fastapi/README.md
├── requirements.txt   # Python dependencies for the example apps
└── venv/              # Python virtual environment (not committed)
```

## Environment setup

Requires Python 3.8+.

1. Create and activate a virtual environment (skip creation if `venv/`
   already exists):

   ```bash
   python -m venv venv
   ```

   ```bash
   # macOS / Linux
   source venv/bin/activate
   ```

   ```powershell
   # Windows (PowerShell)
   venv\Scripts\Activate.ps1
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running an example app

Each snippet lives in its own folder with its own `main.py`. `cd` into the
one you want to run (topic number, then letter), then start it with
Uvicorn — see [example/README.md](example/README.md) for what each topic
and letter covers:

```bash
cd example/1/a
uvicorn main:app --reload
```

Then open:

- [http://127.0.0.1:8000](http://127.0.0.1:8000) — the app itself
- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) — interactive Swagger UI

`--reload` restarts the server on code changes; only use it in development.

## Docs site

`fastapi/` is a separate Next.js + Fumadocs project (its own git repo) with
the full FastAPI walkthrough in English and Tanglish. See
[fastapi/README.md](fastapi/README.md) for how to run it.

## Running curl commands on Windows

Every `curl` command in this repo's docs is written to work as a single
line in **any** shell — Command Prompt (`cmd.exe`), PowerShell, and Git
Bash/WSL alike. If you write your own and it fails, it's almost always
one of these two things:

- **No `\` line continuation.** That's a bash-only convention.
  `cmd.exe` doesn't understand it at all — it runs the first line, then
  tries to run the next line (`-H "..."`) as its own command, which is
  exactly the `'-H' is not recognized as an internal or external
  command` error. Keep the whole `curl` command on one line.
- **No single-quoted JSON bodies.** `-d '{"name": "Alice"}'` works in
  bash, but `cmd.exe` doesn't treat `'` as a quote character at all —
  it splits the argument apart at every space inside it, breaking the
  JSON. Use double quotes for the whole body instead, with the inner
  quotes escaped: `-d "{\"name\": \"Alice\"}"`. This exact form works
  unchanged in `cmd.exe`, PowerShell, and bash.

## Using Postman instead of curl

None of the quoting issues above exist in [Postman](https://www.postman.com/downloads/)
— it's a GUI, so there's no shell to escape anything for. Every example
in this repo maps to the same four fields:

1. **Method** — the dropdown next to the URL bar (`GET`, `POST`, `PUT`,
   `DELETE`) — matches the `-X` flag or the plain `curl URL` in the docs.
2. **URL** — paste it exactly as shown, e.g. `http://127.0.0.1:8000/items`.
3. **Headers tab** — only needed for POST/PUT requests with a body;
   add `Content-Type` / `application/json` (Postman usually sets this
   automatically once you pick the body type below).
4. **Body tab** — select **raw**, then **JSON** from the dropdown on the
   right, and paste the JSON exactly as shown in the docs — with real
   double quotes, no escaping needed (that's only for shells):

   ```json
   {"name": "Laptop", "price": 999.99}
   ```

For a `GET` request with no body (like `/items` or `/items/0`), just
set the method and URL — skip the Headers and Body tabs entirely.

Each exercise's own README (e.g. [example/3/a/README.md](example/3/a/README.md))
has the exact Method/URL/Body for that specific route.

If you'd rather avoid both curl and Postman, every running example also
has a zero-setup option built in: open
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) (Swagger UI)
and use "Try it out" — no client to install, no quoting or JSON syntax
to get right by hand.

## "405 Method Not Allowed"

```
INFO:     127.0.0.1:xxxxx - "GET /items HTTP/1.1" 405 Method Not Allowed
```

This means the route exists, but not for the HTTP method you used — most
routes that accept a JSON body in this repo are declared with
`@app.post(...)`, not `@app.get(...)`. Two common ways to trigger this by
accident:

- **Pasting the URL into a browser's address bar.** A browser always
  sends `GET`. It'll work fine for `GET`-only routes (like `/items/0`),
  but never for a `POST`-only route like `/items` in topic 3 — those
  need curl, Postman, or Swagger UI's "Try it out".
- **Leaving Postman's method dropdown on its default `GET`.** Every new
  Postman request starts as `GET` — check the dropdown next to the URL
  bar and change it to match the route (`POST`, `PUT`, `DELETE`, etc.)
  before sending.

Check the specific exercise's README (e.g. [example/3/a/README.md](example/3/a/README.md))
for which method each route actually expects.
