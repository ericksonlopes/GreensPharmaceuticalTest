from fastapi import APIRouter

from config.database import DATABASE_URL
from src.agents.generate_sales_insights_agent import GenerateSalesInsightsAgent

router = APIRouter()


@router.get("/sales-insights", summary="Gerar insights sobre vendas")
async def get_sales_insights(question: str):
    agent = GenerateSalesInsightsAgent(database_url=DATABASE_URL)
    response = agent.invoke(question)

    return {"question": question, "insight": response}
