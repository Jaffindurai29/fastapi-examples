# 4/d — PATCH, step by step

1. **`ItemPatch` makes its field optional** (`value: Optional[str] = None`)
   — unlike [4/c](../c/STEPS.md)'s `ItemRequest`, where `value` is
   required. That's the whole difference between `PUT` and `PATCH`: PUT
   demands the full representation, PATCH lets you send only what
   changed.

2. **`if patch.value is not None: data[item_index] = patch.value`** —
   only overwrites the slot if the client actually sent a value. An
   empty body (`{}`) leaves the item untouched.

3. **With only one field on this item**, PUT and PATCH behave almost
   identically here — the real difference shows up once a resource has
   several fields and you only want to change one of them.
