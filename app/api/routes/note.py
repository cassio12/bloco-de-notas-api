from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.schemas.note import NoteCreate, NoteResponse, NoteUpdate, NotesListResponse
from app.crud.note import (
    create_note,
    get_note,
    get_notes,
    updated_note,
    delete_note,
)

router = APIRouter(prefix="/notes", tags=["Notes"])

def get_db():
    db = SessionLocal()
    try: 
        yield db 
    finally:
        db.close()

@router.post('/', response_model=NotesListResponse)
def create_note_route(note: NoteCreate, db: Session = Depends(get_db)):
    new = create_note(db, note)
    if not new:
        raise HTTPException(status_code=400, detail="Erro ao criar a nota.")

    notes = get_notes(db)
    return {'message': "Nota criada com sucesso.", "notes": notes}

@router.get('/', response_model=list[NoteResponse])
def get_notes_route(db: Session = Depends(get_db)):
    return get_notes(db)

@router.get('/{note_id}', response_model=NoteResponse)
def get_note_route(note_id: int, db: Session = Depends(get_db)):
    note = get_note(db, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Nenhuma nota encontrada.")

    return note

@router.put('/{note_id}', response_model=NoteResponse)
def update_note_route(note_id: int, note: NoteUpdate, db: Session = Depends(get_db)):
    update = update_note(db, note_id, note)
    if not update: 
        raise HTTPException(status_code=404, detail="Nunhuma nota encontrada para atualizar.")
    return {"message": "Nota atualizada com sucesso.", "note": update}

@router.delete('/{note_id}')
def delete_note_route(note_id: int, db: Session = Depends(get_db)):
    delete = delete_note(db, note_id)
    if not delete:
        raise HTTPException(status_code=404, detail="Nenhuma nota encontrada para deletar.")

    update_note = get_notes(db)

    return {"message": "Nota deletada com sucesso.", "notes": update_note}
    
