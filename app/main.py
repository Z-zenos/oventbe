# import os
# import time

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.core.exception import (
    AccessDeniedError,
    BadRequestError,
    UnauthorizedError,
)
from app.core.response import (
    AccessDeniedResponse,
    BadRequestResponse,
    UnauthorizedResponse,
)

app = FastAPI(title="Roominar", openapi_url="/api/v1/openapi.json")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["content-disposition"],
)

# os.environ["TZ"] = "Asia/Tokyo"
# time.tzset()

app.include_router(api_router, prefix="/api/v1")


@app.get("/healthcheck")
async def healthcheck():
    return "OK"


@app.exception_handler(BadRequestError)
def bad_request_exception_handler(request: Request, exc: BadRequestError):
    return BadRequestResponse(exc.error_code, exc.message, exc.debug_info)


@app.exception_handler(UnauthorizedError)
def unauthorized_exception_handler(request: Request, exc: UnauthorizedError):
    return UnauthorizedResponse(exc.error_code, exc.message, exc.debug_info)


@app.exception_handler(AccessDeniedError)
def access_denied_exception_handler(request: Request, exc: UnauthorizedError):
    return AccessDeniedResponse(exc.error_code, exc.message, exc.debug_info)


@app.exception_handler(ValueError)
async def value_error_exception_handler(request: Request, exc: ValueError):
    return BadRequestResponse(400, str(exc))
