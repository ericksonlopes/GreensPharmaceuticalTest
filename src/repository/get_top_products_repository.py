from sqlalchemy import func
from sqlalchemy.orm import Session

from src.models.sales import Sale


async def get_top_products_internal(limit: int, db: Session):
    """Função auxiliar para ser usada internamente na rota de insights."""
    top_products = db.query(Sale.name, func.count(Sale.name).label("total_sales")) \
        .group_by(Sale.name) \
        .order_by(func.count(Sale.name).desc()) \
        .limit(limit) \
        .all()
    return top_products
