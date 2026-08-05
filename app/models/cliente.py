from pydantic import BaseModel, EmailStr, Field


class Cliente(BaseModel):
    id_cliente: int
    nome: str = Field(min_length=2, max_length=150)
    telefone: str | None = None
    email: EmailStr | None = None