# TechService Integration

Projeto inicial da **UC00614 — Integrar Sistemas de Informação**.

## Objetivo

Demonstrar como aplicações diferentes comunicam através de uma API REST, utilizando HTTP e JSON.

## Passos

```bash
git clone URL_DO_REPOSITORIO
cd techservice-integration
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

Abrir:

- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/api/status
- http://127.0.0.1:8000/api/clientes

Com a API em execução, abrir outro terminal:

```bash
python app/cliente_api.py
```

## Atividade individual

No endpoint `/api/status`, altere:

```python
"ambiente": "desenvolvimento"
```

para:

```python
"ambiente": "Nome do aluno"
```

Depois:

```bash
git add .
git commit -m "feat(api): personaliza endpoint de estado"
```
