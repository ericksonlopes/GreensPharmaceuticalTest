from fastapi import APIRouter, HTTPException

from src.agents.generate_sales_insights_agent import GenerateSalesInsightsAgent
from src.config.settings import settings, logger

router = APIRouter()


@router.get("/sales-insights", summary="Gerar insights sobre vendas")
async def get_sales_insights(question: str):
    logger.info(f"Endpoint /sales-insights acessado. Pergunta: {question}")
    try:
        agent = GenerateSalesInsightsAgent(database_url=settings.DATABASE_URL)
        response = agent.invoke(question)
        logger.info("Insights de vendas gerados com sucesso.")
        return {"question": question, "insight": response}
    except Exception as e:
        logger.error(f"Erro ao gerar insights de vendas para a pergunta '{question}': {e}")
        raise HTTPException(
            status_code=500,
            detail="Erro ao gerar insights de vendas. Por favor, tente novamente mais tarde."
        )
