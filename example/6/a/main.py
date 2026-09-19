import os

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

MYSQL_HOST = os.getenv("MYSQL_HOST", "127.0.0.1")
MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
MYSQL_DB = os.getenv("MYSQL_DB", "fastapi_learn")

# Set DATABASE_URL directly to override everything above (e.g. to point
# at SQLite for a quick local test with no MySQL server at all).
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}",
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class ItemModel(Base):
    __tablename__ = "crud_get_items"
    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(String(255), nullable=False)


Base.metadata.create_all(bind=engine)

# Seed two rows once, so this is testable on its own. Only runs if the
# table is currently empty, so restarting the app doesn't keep adding more.
with SessionLocal() as db:
    if db.query(ItemModel).count() == 0:
        db.add_all([ItemModel(value="first"), ItemModel(value="second")])
        db.commit()

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/items")
def list_items(db: Session = Depends(get_db)):
    rows = db.query(ItemModel).order_by(ItemModel.id).all()
    return [{"id": row.id, "value": row.value} for row in rows]


@app.get("/items/{item_id}")
def get_item(item_id: int, db: Session = Depends(get_db)):
    row = db.get(ItemModel, item_id)
    if row is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": row.id, "value": row.value}
