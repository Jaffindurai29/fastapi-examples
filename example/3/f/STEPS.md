# 3/f — POST, login authentication, step by step

1. **Stand in for a users table with a dict:**
   `fake_users_db = {"admin": "password123"}`.

2. **Look up the submitted username:**
   `correct_password = fake_users_db.get(request.username)`. `.get(...)`
   returns `None` if the username isn't in the dict, instead of raising
   an error.

3. **Check both "doesn't exist" and "wrong password" together:**

   ```python
   if correct_password is None or correct_password != request.password:
       raise HTTPException(status_code=401, detail="Invalid username or password")
   ```

   Both failures get the exact same error message on purpose — telling
   an attacker "that username doesn't exist" (vs. "wrong password") is
   information they shouldn't get.

4. **What's missing, on purpose:** real apps hash passwords before
   storing them (never compare plain text like this) and return a token
   on success instead of just a message. This version keeps the shape of
   a login check visible without those extra moving parts yet.
