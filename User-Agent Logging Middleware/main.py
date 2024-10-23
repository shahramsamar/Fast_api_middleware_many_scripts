import logging
from fastapi import FastAPI, Request

app = FastAPI()

logging.basicConfig(level=logging.INFO)
"""
Example : User-Agent Logging Middleware
This middleware logs the User-Agent header for each incoming request.
This middleware logs the User-Agent header, which can be useful for tracking what types of devices and browsers are accessing your API.
"""
@app.middleware("http")
async def log_user_agent(request: Request, call_next):
    user_agent = request.headers.get("User-Agent", "unknown")
    logging.info(f"Request received from User-Agent: {user_agent}")
    return await call_next(request)

@app.get("/")
async def root():
    return {"message": "User-Agent logged"}
