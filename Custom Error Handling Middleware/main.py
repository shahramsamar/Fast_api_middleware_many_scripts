from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

app = FastAPI()
"""
Example : Custom Error Handling Middleware
This middleware catches any exceptions raised by route handlers and returns a custom error response.
This middleware catches any unhandled exceptions and returns a custom JSON error response, ensuring the API doesn't return a generic 500 error page.
"""
@app.middleware("http")
async def custom_error_handler(request: Request, call_next):
    try:
        response = await call_next(request)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    return response

@app.get("/")
async def root():
    raise Exception("Something went wrong")
