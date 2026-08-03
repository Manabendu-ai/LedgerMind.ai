from langchain_groq import ChatGroq
from langchain.messages import SystemMessage
from langchain.agents import create_agent
import os
from .json_response import JsonFormatResponse
from .system_message import message
from dotenv import load_dotenv

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

class ModelEngine:

    def __init__(self):
        self.model = ChatGroq(
            model = "llama-3.3-70b-versatile"
        )

        self.agent = create_agent(
            model=self.model,
            tools=[],
            system_prompt=message,
            response_format=JsonFormatResponse
        )

        print("[INFO] LLM Model loaded Successfully!")

    def run(self, markdown : str)->JsonFormatResponse:
        return self.agent.invoke(
            {
                "messages" : [
                    {
                        "role" : "user",
                        "content" : markdown
                    }
                ]
            }
        )



    