import requests

BASE_URL = "http://127.0.0.1:8000"

def listar_clientes() -> None:
    try:
        resposta = requests.get(f"{BASE_URL}/api/clientes", timeout=10)
        resposta.raise_for_status()
        print("\nCLIENTES RECEBIDOS DA API")
        print("-" * 40)
        for cliente in resposta.json():
            print(f'{cliente["id"]} - {cliente["nome"]} - {cliente["email"]}')
    except requests.RequestException as erro:
        print(f"Não foi possível consultar a API: {erro}")

if __name__ == "__main__":
    listar_clientes()
