# Set your OpenAI API key

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from PyPDF2 import PdfReader
import openai
from dotenv import load_dotenv
import os
app = FastAPI()
load_dotenv()
# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


class ChatRequest(BaseModel):
    text: str
    question: str


@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    pdf_reader = PdfReader(file.file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return {"text": text}


@app.post("/chat/")
async def chat_with_pdf(request: ChatRequest):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Text from PDF:\n{request.text}\n\nQuestion: {request.question}"}
        ],
        max_tokens=150
    )
    return {"answer": response.choices[0].message['content'].strip()}


@app.get("/")
async def get_index():
    with open("static/index.html") as f:
        return HTMLResponse(f.read())
