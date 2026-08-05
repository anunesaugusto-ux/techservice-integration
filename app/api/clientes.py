from fastapi import APIRouter
from app.database import obter_conexao

router = APIRouter()


@router.get("/", tags=["Clientes"])
def listar_clientes():
    try:
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT id_cliente, nome, email, telefone FROM clientes")
        resultados = cursor.fetchall()
        cursor.close()
        conexao.close()
        return resultados
    except Exception as erro:
        return {"erro": str(erro)}