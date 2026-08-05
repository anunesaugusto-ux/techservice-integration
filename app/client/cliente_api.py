import requests

BASE_URL = "http://127.0.0.1:8000/api/clientes"


def listar_clientes() -> None:
    try:
        resposta = requests.get(f"{BASE_URL}/", timeout=10)
        resposta.raise_for_status()
        print("\nCLIENTES RECEBIDOS DA API")
        print("-" * 40)
        for cliente in resposta.json():
            print(f'{cliente["id_cliente"]} - {cliente["nome"]} - {cliente["email"]}')
    except requests.RequestException as erro:
        print(f"Não foi possível consultar a API: {erro}")


def obter_cliente(id_cliente: int) -> None:
    try:
        resposta = requests.get(f"{BASE_URL}/{id_cliente}", timeout=10)
        resposta.raise_for_status()
        cliente = resposta.json()
        print("\nCLIENTE RECEBIDO DA API")
        print("-" * 40)
        if "erro" in cliente:
            print(cliente["erro"])
        else:
            print(f'{cliente["id_cliente"]} - {cliente["nome"]} - {cliente["email"]} - {cliente["telefone"]}')
    except requests.RequestException as erro:
        print(f"Não foi possível consultar a API: {erro}")


if __name__ == "__main__":
    listar_clientes()
    obter_cliente(1)