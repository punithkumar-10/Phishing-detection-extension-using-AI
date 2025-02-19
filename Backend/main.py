from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from groq import Groq
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

client = Groq(api_key=os.environ["GROQ_API_KEY"])

class URLCheckRequest(BaseModel):
    url: str

@app.post("/check_url")
async def check_url(request: URLCheckRequest):

    prompt = f"Check if the following URL is a phishing site. You have to answer in Yes or No. I am looking for a binary response only. Phishing URL is : {request.url}"

    completion = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[
            {"role": "system", "content": "You are a cybersecurity analyst whose expertise lies in analyzing website URLs and detecting if they are phishing sites or not!"},
            {"role": "user", "content": prompt}
        ]
    )
    return {"result": completion.choices[0].message.content}
