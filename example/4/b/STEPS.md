# 4/b — POST, step by step

1. **`status_code=status.HTTP_201_CREATED`** on the decorator — `POST`
   routes default to `200`; `201` is the more correct code for "a new
   resource was created," and `status.HTTP_201_CREATED` reads clearer
   than the bare number `201`.

2. **`data.append(item.value)`** — adds the new value onto the end of
   the shared array.

3. **`return {"index": len(data) - 1, "value": item.value}`** — tells
   the caller exactly where the new item landed, so a follow-up
   `GET /items/{index}` (or `PUT`/`PATCH`/`DELETE`) knows which index to
   use.
