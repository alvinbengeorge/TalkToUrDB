"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai
from json import loads

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

    def __init__(self):
        self.chat_session = model.start_chat()

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


if __name__ == "__main__":
    session = Session()
    print(
        session.get_response(
            "I need all the data from the table student and find out the number of people who has an average score of 80 or more."
        )
    )
