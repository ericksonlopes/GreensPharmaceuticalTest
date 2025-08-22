# GreensPharmaceuticalTest
Teste Técnico – Desenvolvedor(a) Python

## Visão Geral do Projeto
Este projeto é uma aplicação FastAPI desenvolvida como parte de um teste técnico para Desenvolvedor(a) Python. Ele inclui endpoints para insights de vendas e produtos mais vendidos, utilizando um banco de dados MySQL para persistência de dados.

## Tecnologias Utilizadas
*   Python 3.10+
*   FastAPI
*   Uvicorn
*   MySQL
*   Docker
*   uv (gerenciador de pacotes)

## Configuração do Ambiente

### Pré-requisitos
Certifique-se de ter as seguintes ferramentas instaladas em sua máquina:
*   Docker e Docker Compose
*   Python 3.10+
*   uv (pode ser instalado com `pip install uv`)

### Instalação de Dependências (Localmente)
Se você for rodar a aplicação localmente sem Docker, pode instalar as dependências usando `uv`:

```bash
uv sync
```

## Como Rodar a Aplicação

### Usando Docker Compose (Recomendado)
A maneira mais fácil de rodar a aplicação é usando Docker Compose. Isso irá construir as imagens, configurar o banco de dados e iniciar a aplicação.

1.  **Construa e inicie os contêineres:**
    ```bash
    docker compose up -d --build
    ```
2.  **Verifique os logs (opcional):**
    ```bash
    docker compose logs -f
    ```
3.  **Acesse a aplicação:**
    A aplicação estará disponível em `http://localhost:80`. Você pode acessar a documentação interativa da API (Swagger UI) em `http://localhost:80/docs`.

### Rodando a Aplicação Localmente

1.  **Certifique-se de que as dependências estejam instaladas:**
    ```bash
    uv sync
    ```
2.  **Inicie o banco de dados MySQL (se não estiver usando Docker Compose):**
    Você precisará ter uma instância do MySQL rodando e acessível com as configurações especificadas em `src/config/database.py` ou `.env`.

3.  **Execute a aplicação:**
    ```bash
    uvicorn app:app --host 0.0.0.0 --port 80
    ```
    A aplicação estará disponível em `http://localhost:80`. Você pode acessar a documentação interativa da API (Swagger UI) em `http://localhost:80/docs`.

## Estrutura do Projeto
```
.
├── app.py                      # Ponto de entrada da aplicação FastAPI
├── docker-compose.yml          # Configuração do Docker Compose
├── Dockerfile                  # Definição da imagem Docker
├── generate_fake_data.py       # Script para gerar dados de exemplo
├── pyproject.toml              # Gerenciamento de dependências
├── README.md                   # Este arquivo de documentação
└── src/
    ├── agents/                 # Agentes de processamento (ex: insights de vendas)
    │   └── generate_sales_insights_agent.py
    ├── config/                 # Configurações (ex: banco de dados)
    │   └── database.py
    ├── models/                 # Modelos de dados
    │   └── sales.py
    ├── repository/             # Camada de acesso a dados
    │   └── get_top_products_repository.py
    └── routes/                 # Definição das rotas da API
        ├── sales_insights.py
        └── top_products.py
```

 "fastapi>=0.116.1",
    "langchain-community>=0.3.27",
    "langchain[openai]>=0.3.27",
    "mysql-connector-python>=9.4.0",
    "python-dotenv>=1.1.1",
    "uvicorn>=0.35.0",