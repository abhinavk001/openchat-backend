# A python app to send interact with deepseek-r1 model running in a system
# using ollama.
from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"

class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat")
async def chat(request: ChatRequest):
    payload = {"model": "deepseek-r1:1.5b", "prompt": request.prompt, "stream": False}
    response = requests.post(OLLAMA_ENDPOINT, json=payload)
    return response.json()