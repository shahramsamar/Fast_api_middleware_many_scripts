from fastapi import FastAPI, Request, HTTPException

app = FastAPI()
"""
Example : Request Body Size Limiter
This middleware limits the size of incoming request bodies, raising an exception if the body is too large.
This middleware checks the size of the incoming request body and raises an exception if it exceeds 1KB.
"""
@app.middleware("http")
async def limit_request_size(request: Request, call_next):
    body = await request.body()
    if len(body) > 1024:  # Limit request body size to 1KB
        raise HTTPException(status_code=413, detail="Request body too large")
    return await call_next(request)

@app.post("/upload")
async def upload_file():
    return {"message": "File uploaded successfully"}
