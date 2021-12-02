import spacy
import components
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_health import health

# To force the GPU usage: spacy.require_gpu()
spacy.prefer_gpu()

# Set up the FastAPI app and define the endpoints
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"])

# Health check
def healthy():
    return {"linto-platform-nlp-core": "online"}
app.add_api_route("/health", health([healthy]))

@app.get("/")
def read_root():
    return {"linto-platform-nlp-core": "Hello, World!"}
