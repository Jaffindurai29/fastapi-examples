# fast-api-learn

Learning workspace for [FastAPI](https://fastapi.tiangolo.com/), with small
example apps under `example/` and a bilingual (English + Tanglish) Fumadocs
documentation site under `fastapi/`.

## Project layout

```
fast-api-learn/
├── example/
│   ├── 1/main.py     # minimal "Hello, FastAPI!" app
│   └── 2/main.py     # adds a path parameter (/items/{item_id})
├── fastapi/          # Fumadocs docs site (Next.js) — see fastapi/README.md
├── requirements.txt  # Python dependencies for the example apps
└── venv/             # Python virtual environment (not committed)
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

Each example lives in its own folder with its own `main.py`. `cd` into the
one you want to run, then start it with Uvicorn:

```bash
cd example/1
uvicorn main:app --reload
```

```bash
cd example/2
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
