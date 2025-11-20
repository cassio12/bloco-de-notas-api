from sqlalchemy.orm import Session
from app.models.models import Tag
from app.schemas.tag import TagCreate, TagUpdate


def create_tag(db: Session, tag: TagCreate):
    db_tag = Tag(name=tag.name)
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

def get_tag(db: Session, tag_id: int):
    return db.query(Tag).filter(Tag.id == tag_id).first()

def get_tags(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Tag).offset(skip).limit(limit).all()

def update_tag(db: Session, tag_id: int, tag: TagUpdate):
    db_tag = get_tag(db, tag_id)
    if not db_tag:
        return None
    
    update_data = tag.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_tag, key, value)

    db.commit()
    db.refresh(db_tag)
    return db_tag

def delete_tag(db: Session, tag_id: int):
    db_tag = get_tag(db, tag_id)
    if not db_tag:
        return None

    db.delete(db_tag)
    db.commit()
    return True