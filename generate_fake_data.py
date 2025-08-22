import os
import random

from dotenv import load_dotenv
from faker import Faker
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker

from src.models.sales import Base, Sale

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do banco de dados
MYSQL_ROOT_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD", "root_password")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "my_database")
MYSQL_USER = os.getenv("MYSQL_USER", "root")
# O host aqui deve ser o nome do serviço do MySQL no docker-compose.yml
DATABASE_URL = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_ROOT_PASSWORD}@db:3306/{MYSQL_DATABASE}"

# Inicializar Faker
faker = Faker('pt_BR')

# Base declarativa para os modelos
# Base = declarative_base()

# Definir o modelo da tabela Sales
# class Sale(Base):
#     __tablename__ = 'sales'

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(255), nullable=False)
#     price = Column(Float, nullable=False)
#     date = Column(DateTime, nullable=False)

#     def __repr__(self):
#         return f"<Sale(name='{self.name}', price={self.price}, date='{self.date}')>"

# Função para gerar dados fictícios de vendas de farmácia
def generate_fake_pharmacy_sales(num_records=100):
    sales_data = []
    pharmacy_items = [
        "Paracetamol", "Ibuprofeno", "Amoxicilina", "Dipirona", "Omeprazol",
        "Protetor Solar", "Shampoo Anticaspa", "Condicionador", "Sabonete Líquido",
        "Creme Hidratante", "Vitamina C", "Complexo B", "Curativo Adesivo",
        "Algodão", "Álcool 70%", "Máscara Facial", "Termômetro Digital",
        "Soro Fisiológico", "Lenço Umedecido", "Fralda Descartável"
    ]

    # Gerar um preço fixo para cada item de farmácia
    item_prices = {item: round(random.uniform(5.0, 150.0), 2) for item in pharmacy_items}

    for _ in range(num_records):
        name = random.choice(pharmacy_items)
        price = item_prices[name]
        date = faker.date_time_between(start_date='-1y', end_date='now')
        sales_data.append({'name': name, 'price': price, 'date': date})
    return sales_data

if __name__ == "__main__":
    print("Conectando ao banco de dados...")
    engine = create_engine(DATABASE_URL)

    # Criar a tabela se ela não existir
    Base.metadata.create_all(engine)
    print("Tabela 'sales' verificada/criada.")

    Session = sessionmaker(bind=engine)
    session = Session()

    print("Gerando dados fictícios...")
    fake_sales = generate_fake_pharmacy_sales(200)

    print("Inserindo dados no banco de dados...")
    for sale_data in fake_sales:
        sale = Sale(name=sale_data['name'], price=sale_data['price'], date=sale_data['date'])
        session.add(sale)

    session.commit()
    session.close()
    print(f"{len(fake_sales)} registros de vendas fictícias inseridos com sucesso!")
