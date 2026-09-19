# 3/d — POST, calculator, step by step

1. **Add a third field for which operation to run**: `operation: str`.
2. **Branch on it with `if`/`elif`:**

   ```python
   if request.operation == "add":
       result = request.a + request.b
   elif request.operation == "subtract":
       ...
   ```

3. **Handle the bad-input case explicitly.** Dividing by zero isn't
   something a type hint can catch — `b: float` accepts `0` just fine.
   So the code checks for it and raises a `400` on purpose:

   ```python
   if request.b == 0:
       raise HTTPException(status_code=400, detail="Cannot divide by zero")
   ```

4. **Handle an unknown `operation` too** — the final `else` catches
   anything that isn't one of the four expected words, also as a `400`.
