# 3/a — GET, dynamic name, step by step

1. **Put the value in the path**: `@app.get("/hello/{name}")`.
2. **Read it as a normal string parameter**: `def say_hello(name: str)`.
3. **Build the response using it**: `f"Hello, {name}!"`. Visit
   `/hello/Alice` vs `/hello/Bob` — same route, different output,
   because the value came from the URL.
