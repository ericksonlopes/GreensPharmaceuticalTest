# GreensPharmaceuticalTest
Teste Técnico – Desenvolvedor(a) Python

## Visão Geral do Projeto
Este projeto é uma aplicação FastAPI desenvolvida como parte de um teste técnico para Desenvolvedor(a) Python. Ele inclui endpoints para insights de vendas e produtos mais vendidos, utilizando um banco de dados MySQL.

## Tecnologias Utilizadas
*   Python 3.10+
*   FastAPI
*   Uvicorn
*   MySQL (Docker)
*   Pipenv (gerenciador de pacotes)

## Configuração do Ambiente

### Pré-requisitos
Certifique-se de ter as seguintes ferramentas instaladas em sua máquina:
*   Docker Compose
*   Python 3.10+
*   Pipenv (pode ser instalado com `pip install pipenv`)

### Configuração do Arquivo .env
Este projeto utiliza variáveis de ambiente para configurações sensíveis (como credenciais de banco de dados e chaves de API). Você precisará criar um arquivo `.env` na raiz do projeto (no mesmo diretório do `docker-compose.yml` e `app.py`).

Você pode usar o arquivo `.env_example` como modelo:

1.  **Copie o arquivo de exemplo:**
    ```bash
    cp .env_example .env
    ```
2.  **Edite o arquivo `.env`** e preencha as variáveis conforme necessário. **Importante:** Como a aplicação Python será executada localmente e o MySQL via Docker, o `MYSQL_HOST` deve ser `localhost` (ou `127.0.0.1`).

    Exemplo de `.env`:
    ```
    MYSQL_ROOT_PASSWORD=sua_senha_do_root_do_mysql
    MYSQL_HOST=localhost
    MYSQL_DATABASE=seu_banco_de_dados
    MYSQL_USER=seu_usuario_mysql
    OPENAI_API_KEY=sua_chave_da_api_openai
    ```

    Certifique-se de que os valores `MYSQL_ROOT_PASSWORD`, `MYSQL_DATABASE` e `MYSQL_USER` correspondem às suas configurações do MySQL.

### Instalação de Dependências (Localmente)
Para rodar a aplicação localmente, você precisará instalar as dependências do projeto. O Pipenv gerencia o ambiente virtual e as dependências automaticamente:

1.  **Instale as dependências do projeto:**
    ```bash
    pipenv install
    ```
    Este comando irá criar um ambiente virtual (se ainda não existir) e instalar todas as dependências listadas no `Pipfile`.

2.  **Verifique a instalação do Uvicorn (opcional):**
    Após a instalação das dependências, você pode verificar se o `uvicorn` está disponível no ambiente virtual do Pipenv:
    ```bash
    pipenv run uvicorn --version
    ```
    Se o comando retornar a versão do `uvicorn`, ele foi instalado corretamente.

## Como Rodar a Aplicação

### 1. Iniciar o Banco de Dados MySQL com Docker Compose
Primeiro, inicie o serviço do banco de dados MySQL usando Docker Compose:

```bash
docker compose up -d
```

Você pode verificar os logs para garantir que o MySQL foi iniciado corretamente:
```bash
docker compose logs -f db
```

### 2. Rodar a Aplicação Python Localmente
Após o MySQL estar em execução, você pode iniciar a aplicação Python localmente:

1.  **Popule o banco de dados com dados de exemplo:**
    ```bash
    pipenv run python generate_fake_data.py
    ```
    Isso irá inserir dados falsos na tabela `sales` para que você possa testar a API.

2.  **Execute a aplicação:**
    ```bash
    pipenv run uvicorn app:app --host 0.0.0.0 --port 8000
    ```
    A aplicação estará disponível em `http://localhost:8000`. Você pode acessar a documentação interativa da API (Swagger UI) em `http://localhost:8000/docs`.

## Estrutura do Projeto
```
.
├── app.py                      # Ponto de entrada da aplicação FastAPI
├── docker-compose.yml          # Configuração do Docker Compose (apenas MySQL)
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