from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


class GenerateSalesInsightsAgent:
    def __init__(self, database_url: str):
        self.model = ChatOpenAI(
            model="gpt-4o",
            temperature=0.3
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
    Use as ferramentas necessarias para responder.
    perguntas relacionadas ao sobre vendas de farmácia.
    Perguntas: {q}
    
    Você esta conectado em um banco mysql com dados de vendas de farmácia.
    Responda em pt-br, e seja o mais claro e objetivo possível.
    Se não souber a resposta, diga que não sabe.
    """
        )

    def invoke(self, question: str):
        output = self.agent_executor.invoke(
            {"input": self.prompt_template.format(q=question)}
        )
        return output.get("output")
