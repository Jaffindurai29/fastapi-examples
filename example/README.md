# Examples

Each numbered folder matches a topic from the [docs site](../fastapi),
and each lettered subfolder inside it is one runnable, standalone snippet
from that topic's page — its own `main.py`, run on its own.

| Topic | Docs page |
|---|---|
| [1 — First Steps](1) | [English](../fastapi/content/docs/en/first-steps.mdx) |
| [2 — Path Parameters](2) | [English](../fastapi/content/docs/en/path-parameters.mdx) |
| [3 — Query Parameters](3) | [English](../fastapi/content/docs/en/query-parameters.mdx) |
| [4 — Request Body](4) | [English](../fastapi/content/docs/en/request-body.mdx) |
| [5 — Response & Status Codes](5) | [English](../fastapi/content/docs/en/response-and-status-codes.mdx) |
| [6 — Interactive Docs](6) | [English](../fastapi/content/docs/en/interactive-docs.mdx) |

See the root [README.md](../README.md) for environment setup and how to
run any single sub-example (`cd example/<topic>/<letter>` then
`uvicorn main:app --reload`).
