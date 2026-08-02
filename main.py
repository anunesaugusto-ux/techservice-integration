from fastapi import FastAPI

app = FastAPI(
    title="TechService Integration API",
    description="API inicial da UC00614 — Integração de Sistemas de Informação",
    version="1.0.0",
)

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
        "base_dados": "não conectada",
        "ambiente": "desenvolvimento",
    }

@app.get("/api/clientes", tags=["Clientes"])
def listar_clientes():
    return [
        {"id": 1, "nome": "Ana Martins", "email": "ana.martins@example.com", "telefone": "910000001"},
        {"id": 2, "nome": "Carlos Silva", "email": "carlos.silva@example.com", "telefone": "910000002"},
    ]

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )