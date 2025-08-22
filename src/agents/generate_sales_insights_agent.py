from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from src.config.settings import settings, logger


class GenerateSalesInsightsAgent:
    def __init__(self, database_url: str):
        logger.info("Inicializando GenerateSalesInsightsAgent...")
        self.model = ChatOpenAI(
            model="gpt-4o",
            api_key=settings.OPENAI_API_KEY
        )
        self.db = SQLDatabase.from_uri(database_url)
        self.toolkit = SQLDatabaseToolkit(
            db=self.db,
            llm=self.model
        )
        self.system_message = hub.pull("hwchase17/react")

        self.agent = create_react_agent(
            llm=self.model,
            tools=self.toolkit.get_tools(),
            prompt=self.system_message
        )

        self.agent_executor = AgentExecutor(
            agent=self.agent,
            tools=self.toolkit.get_tools(),
            verbose=True,
            handle_parsing_errors=True
        )

        self.prompt_template = PromptTemplate.from_template(
            """
    Como um assistente de vendas de farmácia, sua tarefa é responder a perguntas sobre vendas, produtos e tendências de mercado.
    Você tem acesso a ferramentas de banco de dados SQL. Use essas ferramentas para consultar as tabelas disponíveis (especialmente 'sales')
    e extrair as informações necessárias para responder às perguntas.
    Por exemplo, para "Quais são os itens que mais venderam?", você deve construir uma query SQL para agregar e ordenar os dados da tabela 'sales'.

    Instruções:
    - Responda em português (Brasil).
    - Seja claro, objetivo e conciso.
    - Se a informação não estiver disponível após a consulta às ferramentas, indique que não sabe a resposta.

    Pergunta do Usuário: {q}
    """
        )

    def invoke(self, question: str):
        logger.info(f"Invocando agente de insights de vendas para a pergunta: {question}")
        try:
            output = self.agent_executor.invoke(
                {"input": self.prompt_template.format(q=question)}
            )
            logger.info("Agente de insights de vendas executado com sucesso.")
            return output.get("output")
        except Exception as e:
            logger.error(f"Erro ao invocar agente de insights de vendas: {e}")
            raise
