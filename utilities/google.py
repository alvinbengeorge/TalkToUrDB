import os
import google.generativeai as genai
from json import loads
from utilities.database import connect_to_mysql, execute_query, MySQLConnection, commit, rollback

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
    "temperature": 1,
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
    def __init__(self, host="localhost", user="root", password=""):
        self.chat_session = model.start_chat()
        self.connection = connect_to_mysql(
            host=host,
            user=user,
            password=password
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
        
    def interpret(self, inp, query: str) -> str:
        print(f"""Interpret the reply from mysql and reply
Query: {query}
Answer: {str(inp)}
            """)
        response = self.chat_session.send_message(
            f"""Interpret the reply from mysql and reply
Query: {query}
Answer: {str(inp)}
            """
        )
        result = loads(response.text)
        if isinstance(result, dict):
            return list(result.values())[0]
        else:
            return result
    
    def __del__(self):
        self.connection.close()

    def execute_query(self, query: str):
        command = self.get_response(query)
        return execute_query(self.connection, command)
    
    def commit(self):
        commit(self.connection)

    def rollback(self):
        rollback(self.connection)