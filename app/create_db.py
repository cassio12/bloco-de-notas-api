from .db.database import engine, Base
from .models.models import Note, Tag

def create_database():
    print("Criando o banco de dados...")
    Base.metadata.create_all(bind=engine)
    print("O banco foi criado com sucesso (arquivo notes.db).")

if __name__ == "__main__": 
    create_database()