# 6/a — GET (MySQL), step by step

1. **Connection settings from environment variables**, with a
   `DATABASE_URL` escape hatch to override everything at once (used for
   testing against SQLite instead of a real MySQL server):

   ```python
   DATABASE_URL = os.getenv(
       "DATABASE_URL",
       f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}",
   )
   ```

2. **The table, as a Python class:**

   ```python
   class ItemModel(Base):
       __tablename__ = "crud_get_items"
       id = Column(Integer, primary_key=True, autoincrement=True)
       value = Column(String(255), nullable=False)
   ```

   `id` is a real, stable, auto-incrementing primary key — unlike the
   array topic, deleting a row never shifts anyone else's `id`.

3. **`Base.metadata.create_all(bind=engine)`** — creates the table if it
   doesn't already exist. Safe to run every time the app starts.

4. **Seed two rows once, only if the table is empty** — so restarting
   the app doesn't keep adding duplicates:

   ```python
   with SessionLocal() as db:
       if db.query(ItemModel).count() == 0:
           db.add_all([ItemModel(value="first"), ItemModel(value="second")])
           db.commit()
   ```

5. **`get_db()` — a dependency that opens one session per request**,
   and always closes it afterward, even if the route raises an error.
   This is the same dependency-injection pattern from earlier topics,
   applied to a real database session.

6. **`GET /items`** queries every row, ordered by `id`. **`GET /items/{item_id}`**
   uses `db.get(ItemModel, item_id)` — SQLAlchemy's shortcut for "fetch
   by primary key," returning `None` if nothing matches.
