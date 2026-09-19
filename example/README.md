# Examples

Each numbered folder matches a topic from the [docs site](../fastapi)
(topic 3 is the exception — a set of practice drills, no single docs
page — see its own [Practice Exercises](../fastapi/content/docs/en/practice)
section), and each lettered subfolder inside it is one runnable,
standalone snippet — its own `main.py`, run on its own. The topic-level
`README.md` is just an index; each lettered subfolder has its own
**README.md** (what it does, how to run it, `curl`/Postman) and
**STEPS.md** (a line-by-line walkthrough of the code itself).

| Topic | Docs page |
|---|---|
| [1 — First Steps](1) | [English](../fastapi/content/docs/en/first-steps.mdx) |
| [2 — Path Parameters](2) | [English](../fastapi/content/docs/en/path-parameters.mdx) |
| [3 — Practice](3) | [English](../fastapi/content/docs/en/practice) (own sidebar section, one page per drill) |

See the root [README.md](../README.md) for environment setup and how to
run any single sub-example (`cd example/<topic>/<letter>` then
`uvicorn main:app --reload`).
