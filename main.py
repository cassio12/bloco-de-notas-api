from fastapi import FastAPI
from app.api.routes.note import router as notes_router
from app.api.routes.tag import router as tags_router

app = FastAPI()

app.include_router(notes_router)
app.include_router(tags_router)