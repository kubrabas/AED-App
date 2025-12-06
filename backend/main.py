from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import json

app = FastAPI()

# Şimdilik her yerden gelen isteğe izin veriyoruz (localhost:8000 vs)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # ileride burayı sıkılaştırırız
    allow_methods=["*"],
    allow_headers=["*"],
)

# aeds.json dosyasının yolu
DATA_FILE = Path(__file__).resolve().parent.parent / "frontend" / "aeds.json"


@app.get("/aeds")
def get_aeds():
    """AED listesini frontend klasöründeki aeds.json'dan oku ve geri döndür."""
    text = DATA_FILE.read_text(encoding="utf-8")
    return json.loads(text)


@app.get("/")
def root():
    return {"status": "ok", "message": "AED backend çalışıyor"}
