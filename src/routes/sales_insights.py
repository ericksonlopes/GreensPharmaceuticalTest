from fastapi import APIRouter

from src.config.settings import settings
from src.agents.generate_sales_insights_agent import GenerateSalesInsightsAgent

router = APIRouter()
 

@router.get("/sales-insights", summary="Gerar insights sobre vendas")
async def get_sales_insights(question: str):
    agent = GenerateSalesInsightsAgent(database_url=settings.DATABASE_URL)
    response = agent.invoke(question)

    return {"question": question, "insight": response}
