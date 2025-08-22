from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.config.database import get_db
from src.config.settings import logger
from src.repository.get_top_products_repository import get_top_products_internal

router = APIRouter()


@router.get("/top-products", summary="Obter os produtos mais vendidos")
async def get_top_products(limit: int = 10, db: Session = Depends(get_db)):
    """Retorna uma lista dos produtos mais vendidos, baseada na contagem de vendas."""
    logger.info(f"Endpoint /top-products acessado. Limite: {limit}")
    try:
        top_products = await get_top_products_internal(limit, db)
        logger.info("Produtos mais vendidos obtidos com sucesso.")
        return {"top_products": top_products}
    except Exception as e:
        logger.error(f"Erro ao obter os produtos mais vendidos: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro interno do servidor")
