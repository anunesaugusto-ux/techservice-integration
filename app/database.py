import os

import mysql.connector
from dotenv import load_dotenv
from mysql.connector import MySQLConnection

load_dotenv()


def obter_conexao() -> MySQLConnection:
    campos_obrigatorios = [
        "DB_HOST",
        "DB_PORT",
        "DB_NAME",
        "DB_USER",
        "DB_PASSWORD",
    ]

    ausentes = [campo for campo in campos_obrigatorios if not os.getenv(campo)]
    if ausentes:
        raise RuntimeError(
            "Configuração incompleta. Variáveis ausentes: "
            + ", ".join(ausentes)
        )

    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", "3306")),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        charset="utf8mb4",
        autocommit=True,
        connection_timeout=10,
    )


def testar_conexao() -> bool:
    conexao = None

    try:
        conexao = obter_conexao()
        return conexao.is_connected()
    except Exception:
        return False
    finally:
        if conexao is not None and conexao.is_connected():
            conexao.close()
