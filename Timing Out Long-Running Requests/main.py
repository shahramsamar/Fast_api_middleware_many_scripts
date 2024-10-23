import asyncio
from fastapi import FastAPI, Request, HTTPException

app = FastAPI()

"""
Example : Timing Out Long-Running Requests
This middleware imposes a timeout on requests that take too long to process.
This middleware limits request processing time to 5 seconds, raising a 504 Gateway Timeout if it exceeds this limit.
"""

@app.middleware("http")
async def timeout_middleware(request: Request, call_next):
    try:
        response = await asyncio.wait_for(call_next(request), timeout=5)  # Timeout set to 5 seconds
    except asyncio.TimeoutError:
        raise HTTPException(status_code=504, detail="Request took too long to process")
    return response

@app.get("/slow")
async def slow_endpoint():
    await asyncio.sleep(10)  # Simulate a long-running request
    return {"message": "This is a slow response"}
