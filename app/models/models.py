from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    Table,
    ForeignKey,
    func
)
from sqlalchemy.orm import relationship
from app.db.database import Base

notes_tags = Table(
    "notes_tags",
    Base.metadata,
    Column("note_id", Integer, ForeignKey("notes.id", ondelete="CASCADE"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True),
)

class Note(Base): 
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    tags = relationship("Tag", secondary=notes_tags, back_populates="notes", lazy="joined")


class Tag(Base): 
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)

    notes = relationship("Note", secondary=notes_tags, back_populates="tags", lazy="joined")