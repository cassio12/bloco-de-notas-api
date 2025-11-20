from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.schemas.tag import TagCreate, TagResponse, TagUpdate
from app.crud.tag import (
    create_tag,
    get_tag,
    get_tags,
    update_tag,
    delete_tag,
)

router = APIRouter(prefix="/tags", tags=["Tags"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/', response_model=TagResponse)
def create_tag_route(tag: TagCreate, db: Session = Depends(get_db)):
    new = create_tag(tag, db)
    if not new: 
        raise HTTPException(status_code=400, detail="Já existe uma Tag com esse nome.")
    
    return {"message": "Tag criada com sucesso.", "tag": new}

@router.get('/', response_model=list[TagResponse])
def get_tags_route(db: Session = Depends(get_db)):
    return get_tags(db)

@router.get('/{tag_id}', response_model=TagResponse)
def get_tag_route(tag_id: int, db: Session = Depends(get_db)):
    tag = get_tag(db, tag_id)
    if not tag:
        raise HTTPException(status_code=404, detail="Nenhuma Tag encontrada.")

    return tag

@router.put('/{tag_id}', response_model=TagResponse)
def update_tag_route(tag_id: int, tag: TagUpdate, db: Session = Depends(get_db)):
    update = update_tag(db, tag_id, tag)
    if not update:
        raise HTTPException(status_code=404, detail="Nenhuma Tag encontrada para atualizar.")

    return {"message": "Tag atualizada com sucesso.", "tag": update}

@router.delete('/{tag_id}')
def delete_tag_route(tag_id: int, db: Session = Depends(get_db)):
    delete = delete_tag(db, tag_id)
    if not delete:
        raise HTTPException(status_code=404, detail="Nenhuma Tag encontrada para deletar.")

    update_tag = get_tags(db)

    return {"message": "Tag deletada com sucesso.", "tag": update_tag}