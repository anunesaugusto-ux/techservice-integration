from fastapi import APIRouter, HTTPException, status
from mysql.connector import Error

from app.database import obter_conexao
from app.models.cliente import Cliente

router = APIRouter()


@router.get("/", response_model=list[Cliente], tags=["Clientes"])
def listar_clientes():
    conexao = None
    cursor = None
    try:
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(
            "SELECT id_cliente, nome, email, telefone FROM clientes WHERE status = 1 ORDER BY nome"
        )
        return cursor.fetchall()
    except Error as erro:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao consultar clientes: {erro}")
    finally:
        if cursor is not None:
            cursor.close()
        if conexao is not None and conexao.is_connected():
            conexao.close()


@router.get("/{id_cliente}", response_model=Cliente, tags=["Clientes"])
def obter_cliente(id_cliente: int):
    conexao = None
    cursor = None
    try:
        conexao = obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(
            "SELECT id_cliente, nome, email, telefone FROM clientes WHERE id_cliente = %s AND status = 1",
            (id_cliente,)
        )
        resultado = cursor.fetchone()
        if resultado is None:
            raise HTTPException(status_code=404, detail=f"Cliente com id {id_cliente} não encontrado")
        return resultado
    except Error as erro:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao consultar cliente: {erro}")
    finally:
        if cursor is not None:
            cursor.close()
        if conexao is not None and conexao.is_connected():
            conexao.close()

@router.put("/{id_cliente}", tags=["Clientes"])
def editar_cliente(id_cliente: int, cliente: Cliente):
    conexao = None
    cursor = None
    try:
        conexao = obter_conexao()
        cursor = conexao.cursor()
        
        cursor.execute(
            """
            UPDATE clientes 
            SET nome = %s, email = %s, telefone = %s 
            WHERE id_cliente = %s AND status = 1
            """,
            (cliente.nome, cliente.email, cliente.telefone, id_cliente)
        )
        conexao.commit()
        
        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail="Cliente não encontrado."
            )
 
        return {
            "mensagem": "Cliente atualizado com sucesso."
        }
    except Error as erro:
        if conexao:
            conexao.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao atualizar cliente: {erro}"
        )
    finally:
        if cursor is not None:
            cursor.close()
        if conexao is not None and conexao.is_connected():
            conexao.close()