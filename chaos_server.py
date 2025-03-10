import os
import uvicorn
import requests  # Přidání importu pro knihovnu requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Třída pro požadavky
class ChatRequest(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"message": "Chaos AI běží!"}

@app.post("/chat")
def chat_chaos(request: ChatRequest):
    user_message = request.message
    response = f"Chaos říká: {user_message[::-1]}"  # Odpověď otočí text
    return {"response": response}

@app.get("/install_libraries")
def install_libraries():
    os.system("pip install -r requirements.txt")
    return {"message": "Knihovny byly úspěšně staženy a aktivovány."}

PORT = int(os.getenv("PORT", 8080))

if __name__ == "__main__":
    os.system("pip install -r requirements.txt")  # Zajištění instalace knihoven při spuštění
    uvicorn.run(app, host="0.0.0.0", port=PORT)


