# 3/b — POST, dynamic name, step by step

1. **Same idea as [3/a](../a/STEPS.md), but the value comes from a JSON
   body instead of the URL.** Define a small model for it:

   ```python
   class NameRequest(BaseModel):
       name: str
   ```

2. **Read it as the route's parameter**: `def say_hello(request: NameRequest)`,
   then use `request.name` the same way 3/a used `name` directly.
