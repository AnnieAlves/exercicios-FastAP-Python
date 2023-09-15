from fastapi import FastAPI, HTTPException
from uuid import UUID
from typing import List
from models import User, Role

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("465c5524-35b5-4941-9906-dbb4e5691e07"),
        first_name="Luciana",
        last_name="Silva",
        email="email@gmail.com",
        role=[Role.role_1]
    ),
    User(
        id=UUID("d0c4c133-7187-486c-b104-2a022324a639"),
        first_name="Cynthia",
        last_name="Zanoni",
        email="email@gmail.com",
        role=[Role.role_2]
    ),
    User(
        id=UUID("b5a78b28-7959-4970-80f1-1b7faf28779a"),
        first_name="Camila",
        last_name="Silva",
        email="email@gmail.com",
        role=[Role.role_3]
    )

]

@app.get('/')

async def root():
    return {"message": "Olá, Womakers"}

@app.get('/api/users')
async def get_users():
    return db

@app.get("/api/users/{id}")
async def get_user(id: UUID):
    for user in db:
        if user.id == id:
            return user
    return {"Message": "Usuário não encontrado"}

@app.post("/api/users")
async def add_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/users/{id}")
async def remove_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return {"Message": "Usuário removido com sucesso" }
    raise HTTPException(
        status_code=404,
        detail=f"Usuário com id {id} não encontrado"
    )
        

@app.put("/api/users/{id}")
async def upgrade_user(id: UUID, updated_user: User):
    for user in db:
        if user.id == id:
            user.first_name = updated_user.first_name
            user.last_name = updated_user.last_name
            user.email = updated_user.email
            user.role = updated_user.role
            return {"Message": "Usuário atualizado com sucesso"}
    raise HTTPException(
        status_code=404,
        detail=f"Usuário com id {id} não encontrado"
    )


