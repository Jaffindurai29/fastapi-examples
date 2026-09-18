# fast-api-learn

Learning workspace for [FastAPI](https://fastapi.tiangolo.com/), with small
example apps under `example/` and a bilingual (English + Tanglish) Fumadocs
documentation site under `fastapi/`.

## Project layout

```
fast-api-learn/
├── example/           # one folder per docs topic, lettered subfolders per snippet
│   ├── 1/a, 1/b       # First Steps
│   ├── 2/a, 2/b, 2/c  # Path Parameters
│   ├── 3/a..3/d       # Query Parameters
│   ├── 4/a..4/c       # Request Body
│   ├── 5/a..5/c       # Response & Status Codes
│   └── 6/a            # Interactive Docs
│   (see example/README.md for the full topic → docs-page map)
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
cd example/2/a
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
