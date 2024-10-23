import time
from fastapi import FastAPI, Request, HTTPException

app = FastAPI()

RATE_LIMIT = 5  # Max 5 requests
TIME_WINDOW = 60  # Time window in seconds

clients = {}
"""
Example : Rate Limiting Middleware.
This example implements simple rate limiting, restricting the number of requests a client can make within a time window.
This middleware tracks request times and denies further requests if they exceed the rate limit within the time window.
"""
@app.middleware("http")
async def rate_limit(request: Request, call_next):
    client_ip = request.client.host
    current_time = time.time()
    
    if client_ip not in clients:
        clients[client_ip] = []
    
    request_times = clients[client_ip]
    request_times = [t for t in request_times if t > current_time - TIME_WINDOW]
    
    if len(request_times) >= RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Too many requests")
    
    request_times.append(current_time)
    clients[client_ip] = request_times
    
    return await call_next(request)

@app.get("/")
async def root():
    return {"message": "You are within the rate limit"}
