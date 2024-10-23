from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware

app = FastAPI()
"""
Example : Gzip Compression Middleware
FastAPI has a built-in middleware for compressing responses using Gzip.
This middleware compresses responses larger than 1000 bytes using Gzip, which can help reduce network bandwidth usage.
"""
app.add_middleware(GZipMiddleware, minimum_size=1000)

@app.get("/")
async def root():
    return {"message": "This response will be compressed if it's bigger than 1000 bytes"}
