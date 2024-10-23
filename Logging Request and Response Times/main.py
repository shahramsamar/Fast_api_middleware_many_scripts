import time
from fastapi import FastAPI, Request

app = FastAPI()


# Example 1: Logging Request and Response Times
# This middleware logs the time taken to process each request and adds a custom header X-Process-Time to the response.
@app.middleware("http")
async def log_request_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

@app.get("/")
async def root():
    return {"message": "Hello World"}
