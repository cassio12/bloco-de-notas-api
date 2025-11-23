from sqlalchemy.orm import Session
from app.models.models import Note
from app.schemas.note import NoteCreate, NoteUpdate

def create_note(db: Session, note: NoteCreate): 
    tags = []
    if note.tags:
        tags = db.query(Tag).filter(Tag.id.in_(note.tags)).all()

    db_note = Note(
        title=note.title,
        content=note.content,
        tags=tags
    )
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def get_note(db: Session, note_id: int): 
    return db.query(Note).filter(Note.id == note_id).first()

def get_notes(db: Session, skip: int = 0, limit: int = 100): 
    return db.query(Note).offset(skip).limit(limit).all()

def updated_note(db: Session, note_id: int, note: NoteUpdate):
    db_note = get_note(db, note_id)
    if not db_note:
        return None

    update_data = note.dict(exclude_unset=True)
    for key, value in update_data.items():
        if key != "tags": 
            setattr(db_note, key, value)
            
    if "tags" in update_data and update_data["tags"] is not None:
        new_tags = db.query(Tag).filter(Tag.id.in_(update_data["tags"])).all()
        db_note.tags = new_tags

    db.commit()
    db.refresh(db_note)
    return db_note

def delete_note(db: Session, note_id: int):
    db_note = get_note(db, note_id)
    if not db_note:
        return None

    db.delete(db_note)
    db.commit()
    return True