from fastapi import FastAPI, Request

app = FastAPI()


"""
 Example : Adding a Custom Header to All Responses
 This middleware adds a custom header to all responses.
"""

@app.middleware("http")
async def add_custom_header(request: Request, call_next):
    response = await call_next(request)
    response.headers['X-Custom-Header'] = "This is a custom header"
    return response

@app.get("/")
async def root():
    return {"message": "Hello with custom header"}
