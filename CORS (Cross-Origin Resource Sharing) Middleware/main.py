from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
"""
Example : CORS (Cross-Origin Resource Sharing) Middleware
FastAPI provides a built-in middleware for handling CORS.
This middleware allows you to control which domains, methods, and headers are allowed to access your FastAPI server.
"""
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
async def root():
    return {"message": "CORS-enabled API"}
