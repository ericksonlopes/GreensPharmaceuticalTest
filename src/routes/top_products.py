from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.config.database import get_db
from src.repository.get_top_products_repository import get_top_products_internal

router = APIRouter()


@router.get("/top-products", summary="Obter os produtos mais vendidos")
async def get_top_products(limit: int = 10, db: Session = Depends(get_db)):
    """Retorna uma lista dos produtos mais vendidos, baseada na contagem de vendas."""
    top_products = await get_top_products_internal(limit, db)
    return {"top_products": top_products}
