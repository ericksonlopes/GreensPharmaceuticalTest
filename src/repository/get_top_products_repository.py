from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.config.settings import logger
from src.models.sales import Sale


async def get_top_products_internal(limit: int, db: Session):
    logger.info(f"Iniciando a busca pelos {limit} produtos mais vendidos.")
    try:
        top_products = db.query(Sale.name, func.count(Sale.name).label("total_sales")) \
            .group_by(Sale.name) \
            .order_by(func.count(Sale.name).desc()) \
            .limit(limit) \
            .all()

        if not top_products:
            logger.warning("Nenhum produto encontrado na base de dados.")

        logger.info(f"Busca pelos {limit} produtos mais vendidos finalizada com sucesso.")
        return [{"name": name, "total_sales": total_sales} for name, total_sales in top_products]

    except SQLAlchemyError as e:
        logger.error(f"Erro no banco de dados ao buscar os produtos mais vendidos: {e}")
        raise e

    except Exception as e:
        logger.error(f"Erro inesperado ao buscar os produtos mais vendidos: {e}")
        raise e
