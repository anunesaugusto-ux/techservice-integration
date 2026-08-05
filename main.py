from fastapi import FastAPI
from app.database import testar_conexao
from app.api import clientes

app = FastAPI(
    title="TechService Integration API",
    description="API inicial da UC00614 — Integração de Sistemas de Informação",
    version="1.0.0",
)

app.include_router(clientes.router, prefix="/api/clientes", tags=["Clientes"])


@app.get("/", tags=["Sistema"])
def inicio():
    return {
        "sistema": "TechService Integration",
        "versao": "1.0.0",
        "mensagem": "API em funcionamento",
    }


@app.get("/api/status", tags=["Sistema"])
def consultar_status():
    return {
        "api": "online",
        "base_dados": "conectada" if testar_conexao() else "não conectada",
        "ambiente": "desenvolvimento",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )