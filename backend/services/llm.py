from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import json
import re

load_dotenv() 

#here we have accept the incoming context from rag pipeline and provided to the LLM so that it could give output on the basis of it.
class LLMService:
    def __init__(self):
        groq_api_key = os.getenv("GROQ_API_KEY")
        if not groq_api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables!")

        self.llm = ChatGroq(
            groq_api_key=groq_api_key,
            model_name="llama-3.1-8b-instant"
        )

    def generate(self, query, context):
        prompt = f"""
    You are a helpful AI assistant.

    Answer the question ONLY using the context below.

    Rules:
    - Be clear and concise
    - Do NOT repeat the question
    - Do NOT generate multiple answers
    - If answer is not in context, say: "I don't know based on the provided document"

    Context:
    {context}

    Question:
    {query}

    Answer:
    """

        response = self.llm.invoke([HumanMessage(content=prompt)])
        return response.content


# booking

    def extract_booking(self, query: str):
        prompt = f"""
    You are an information extraction system.

    Extract booking details from the text below.

    Text:
    "{query}"

    Return ONLY valid JSON. Do NOT add explanation.

    Format:
    {{
        "name": "string or null",
        "email": "string or null",
        "date": "string or null",
        "time": "string or null"
    }}
    """

        response = self.llm.invoke([HumanMessage(content=prompt)])
        text = response.content.strip()

        print("LLM RAW:", text)

        try:
            return json.loads(text)

        except:
            pass

        try:
            json_match = re.search(r'\{[^{}]*\}', text)

            if json_match:
                return json.loads(json_match.group())

        except Exception as e:
            print("Booking extraction error:", e)

        return None
