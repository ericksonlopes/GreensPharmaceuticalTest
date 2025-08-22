from dotenv import load_dotenv, find_dotenv
from fastapi import FastAPI

from src.routes import top_products, sales_insights

load_dotenv(find_dotenv())

app = FastAPI(
    title="API de Vendas de Farmácia",
    description="API para análise de dados de vendas de farmácia e insights.",
    version="1.0.0",
)

app.include_router(top_products.router)
app.include_router(sales_insights.router)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
