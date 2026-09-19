import os
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
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
    __tablename__ = "crud_react_items"
    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(String(255), nullable=False)


Base.metadata.create_all(bind=engine)

with SessionLocal() as db:
    if db.query(ItemModel).count() == 0:
        db.add_all([ItemModel(value="first"), ItemModel(value="second")])
        db.commit()

app = FastAPI()

# The React dev server (Vite) runs on a different origin/port than this
# API, so the browser needs explicit permission to read the response.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class ItemRequest(BaseModel):
    value: str


class ItemPatch(BaseModel):
    value: Optional[str] = None


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


@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(item: ItemRequest, db: Session = Depends(get_db)):
    row = ItemModel(value=item.value)
    db.add(row)
    db.commit()
    db.refresh(row)
    return {"id": row.id, "value": row.value}


@app.put("/items/{item_id}")
def replace_item(item_id: int, item: ItemRequest, db: Session = Depends(get_db)):
    row = db.get(ItemModel, item_id)
    if row is None:
        raise HTTPException(status_code=404, detail="Item not found")
    row.value = item.value
    db.commit()
    db.refresh(row)
    return {"id": row.id, "value": row.value}


@app.patch("/items/{item_id}")
def update_item(item_id: int, patch: ItemPatch, db: Session = Depends(get_db)):
    row = db.get(ItemModel, item_id)
    if row is None:
        raise HTTPException(status_code=404, detail="Item not found")
    if patch.value is not None:
        row.value = patch.value
    db.commit()
    db.refresh(row)
    return {"id": row.id, "value": row.value}


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    row = db.get(ItemModel, item_id)
    if row is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(row)
    db.commit()
