# Notes API – Documentação Completa

Este documento descreve toda a estrutura, decisões e fluxo da API de Notas e Tags construída com **FastAPI**, **SQLAlchemy** e **SQLite**.

---

## 📌 Visão Geral
A API permite criar, listar, atualizar e deletar **Notas**, com suporte a associação de **Tags** (relação Many-to-Many).

Tecnologias utilizadas:
- FastAPI
- SQLAlchemy ORM
- SQLite
- Pydantic
- Uvicorn

---

## 📁 Estrutura do Projeto
```
app/
 ├── api/
 │    └── routes/
 │         ├── note.py
 │         └── tag.py
 ├── crud/
 │    ├── note.py
 │    └── tag.py
 ├── db/
 │    ├── database.py
 │    └── models.py
 ├── schemas/
 │    ├── note.py
 │    └── tag.py
 └── main.py
```

---

## 🧱 Banco de Dados
### **Tabelas criadas**
- `notes`
- `tags`
- `notes_tags` (tabela de associação)

### **Comandos usados para recriar o banco**
```
rm .notes.db
python3
>>> from app.db.database import Base, engine
>>> Base.metadata.create_all(bind=engine)
```

---

## 🧩 Models (SQLAlchemy)
### Note
- id (int)
- title (str)
- content (str | None)
- created_at
- updated_at
- tags → relação Many-to-Many

### Tag
- id (int)
- name (str)
- notes → relação Many-to-Many

---

## 📦 Schemas (Pydantic)
### Note
- NoteBase
- NoteCreate
- NoteUpdate
- NoteResponse

### Tag
- TagBase
- TagCreate
- TagUpdate
- TagResponse

Todos com `orm_mode = True`.

---

## 🔧 CRUD
### Notes
- `get_notes`
- `get_note_by_id`
- `create_note`
- `update_note`
- `delete_note`

### Tags
- `get_tags`
- `get_tag_by_id`
- `create_tag`
- `update_tag`
- `delete_tag`


---

## 🌐 Rotas
### `/notes`
- **GET** `/notes` – Lista todas as notas
- **POST** `/notes` – Cria uma nota
- **GET** `/notes/{id}` – Obter nota por ID
- **PUT** `/notes/{id}` – Atualizar nota
- **DELETE** `/notes/{id}` – Deletar nota

### `/tags`
- **GET** `/tags` – Lista todas as tags
- **POST** `/tags` – Cria uma tag
- **GET** `/tags/{id}` – Obter tag por ID
- **PUT** `/tags/{id}` – Atualizar tag
- **DELETE** `/tags/{id}` – Deletar tag

---

## 🧪 Testes via Postman
### Exemplo de criação de nota com tags
```json
{
  "title": "Minha primeira nota",
  "content": "Aprendendo FastAPI",
  "tags": [1, 2]
}
```

---

## ⚙️ Execução do Servidor
```
uvicorn app.main:app --reload
```
A API ficará disponível em:
```
http://localhost:8000
```

---

## 📘 Observações Importantes
- Atualizações **podem retornar os dados atualizados**, dependendo da implementação.
- Deletes devem retornar apenas uma mensagem ou nada.
- Relações Many-to-Many exigem manipulação tanto no CRUD quanto nas rotas.

---

## 🏁 Conclusão
Este README cobre toda a configuração, estrutura, decisões e implementação da API de Notas e Tags.

Se quiser, podemos:
- adicionar exemplos completos de requisições
- adicionar uma sessão de troubleshooting
- adicionar arquitetura visual do fluxo
- adicionar versão com Markdown mais sofisticado

