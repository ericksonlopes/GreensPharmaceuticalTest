# GreensPharmaceuticalTest

Este projeto é uma aplicação de backend para análise de vendas de uma empresa farmacêutica. Ele fornece insights sobre os produtos mais vendidos e tendências de vendas, utilizando um agente de inteligência artificial para gerar essas análises.

## Instalação

Para configurar o ambiente de desenvolvimento, siga os passos abaixo:
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/GreensPharmaceuticalTest.git
   cd GreensPharmaceuticalTest
   ```

2. Certifique-se de que configurou o arquivo `.env` utilize o arquivo `.env.example` como modelo. Este arquivo deve conter as variáveis de ambiente necessárias para a aplicação, como as credenciais do banco de dados e outras configurações.


3. Inicie os serviços do Docker Compose (que inclui o banco de dados):
   ```bash
   docker-compose up -d
   ```

## Uso

A API esará disponível em `http://localhost:8000/` (ou na porta configurada nas variáveis de ambiente).

Você pode acessar a documentação interativa da API (Swagger UI) em `http://localhost:8000/docs` para explorar os endpoints e testar as requisições.

### Endpoints da API

- `/top_products`: Retorna os produtos mais vendidos.
- `/sales_insights`: Gera insights sobre as vendas utilizando um agente de IA.

## Estrutura do Projeto

A estrutura principal do projeto é a seguinte:

```
.
├── app.py                      # Ponto de entrada da aplicação
├── dockerfile                  # Dockerfile para build da imagem
├── docker-compose.yml          # Configuração Docker Compose para serviços
├── generate_fake_data.py       # Script para gerar dados de teste
├── Pipfile                     # Gerenciamento de dependências (Pipenv)
├── Pipfile.lock                # Bloqueio de dependências (Pipenv)
└── src/
    ├── agents/                 # Contém os agentes de IA
    │   └── generate_sales_insights_agent.py # Agente para gerar insights de vendas
    ├── config/                 # Configurações da aplicação
    │   ├── database.py         # Configuração do banco de dados
    │   └── settings.py         # Variáveis de ambiente e configurações gerais
    ├── models/                 # Modelos de dados
    │   └── sales.py            # Modelo para dados de vendas e produtos
    ├── repository/             # Camada de acesso a dados
    │   └── get_top_products_repository.py # Repositório para obter produtos mais vendidos
    └── routes/                 # Definição das rotas da API
        ├── sales_insights.py   # Rotas para insights de vendas
        └── top_products.py     # Rotas para produtos mais vendidos
```

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
