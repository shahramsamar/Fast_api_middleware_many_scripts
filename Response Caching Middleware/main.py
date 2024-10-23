import time
from fastapi import FastAPI, Request

app = FastAPI()

cache = {}
"""
Example : Response Caching Middleware
This middleware caches responses for specific routes to improve performance.
This middleware caches responses based on the request path, allowing subsequent requests to retrieve the cached response.
"""
@app.middleware("http")
async def cache_response(request: Request, call_next):
    if request.url.path in cache:
        return cache[request.url.path]
    
    response = await call_next(request)
    cache[request.url.path] = response
    return response

@app.get("/")
async def root():
    time.sleep(2)  # Simulate slow processing
    return {"message": "Response with caching"}
