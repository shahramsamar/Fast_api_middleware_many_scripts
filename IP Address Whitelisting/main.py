from fastapi import FastAPI, Request, HTTPException

app = FastAPI()

WHITELISTED_IPS = {"127.0.0.1", "192.168.1.1"}

"""
Example : IP Address Whitelisting
This middleware restricts access to the API by checking if the request is coming from a whitelisted IP address.
This middleware checks the client’s IP address and blocks the request if the IP is not in the WHITELISTED_IPS set.
"""
@app.middleware("http")
async def ip_whitelist(request: Request, call_next):
    client_ip = request.client.host
    if client_ip not in WHITELISTED_IPS:
        raise HTTPException(status_code=403, detail="Access denied: IP not whitelisted")
    return await call_next(request)

@app.get("/")
async def root():
    return {"message": "Request from a whitelisted IP"}
