from fastapi import FastAPI

from src.routes import top_products, sales_insights
from src.config.settings import logger

logger.info("Iniciando a aplicação FastAPI...")

app = FastAPI(
    title="API de Vendas de Farmácia",
    description="API para análise de dados de vendas de farmácia e insights.",
    version="1.0.0"
)

app.include_router(top_products.router)
app.include_router(sales_insights.router)
