import os
import uvicorn
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

PORT = int(os.getenv("PORT", 8080))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)


