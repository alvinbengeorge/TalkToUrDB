import os
import google.generativeai as genai
from json import loads
from utilities.database import connect_to_mysql, execute_query, MySQLConnection, commit, rollback
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)


class Session:
    def __init__(self, host="localhost", user="root", password="", database="test"):
        self.chat_session = model.start_chat()
        self.connection = connect_to_mysql(
            host=host,
            user=user,
            password=password,
            database=database
        )

    def get_response(self, inp: str) -> str:
        response = self.chat_session.send_message(
            f"""Write an SQL command:
            {inp}

        Just the command"""
        )

        result = loads(response.text)
        if isinstance(result, dict):
            return list(result.values())[0]
        else:
            return result
        
    def interpret(self, inp, query: str, command: str = "") -> str:
        print(f"""Interpret the reply
Query: {query}
Command: {command}
Answer: {str(inp)}
            """)
        response = self.chat_session.send_message(
            f"""Interpret the reply
Note: Keep it small and try to show tables if tuples come
Query: {query}
Command: {command}
Answer: {str(inp)}
            """,
            generation_config={
                "temperature": 0,
                "top_p": 0.95,
                "top_k": 64,
                "max_output_tokens": 8192,
                "response_mime_type": "text/plain",
            }
        )
        return response.text
    
    def __del__(self):
        self.connection.close()

    def execute_query(self, query: str):
        command = self.get_response(query)
        return execute_query(self.connection, command), command
    
    def commit(self):
        commit(self.connection)

    def rollback(self):
        rollback(self.connection)