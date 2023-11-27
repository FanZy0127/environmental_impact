from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.routers.router import router

app = FastAPI(
    title="EnvironmentalImpact",
    description=("Module permettant d'évaluer l'impact environnemental d'une entreprise."),
    version="1.0.0",
)

@app.exception_handler(ValueError)
async def value_exception_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "ok": False,
            "detail": str(exc),
        },
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request, exc: RequestValidationError
):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "ok": False,
            "detail": " | ".join(map(lambda e: e["msg"], exc.errors())),
        },
    )


@app.exception_handler(AssertionError)
async def assert_exception_handler(request: Request, exc: AssertionError):
    exc_split = str(exc).split(",", 1)
    (status_code, msg) = (
        (int(exc_split[0]), exc_split[1].strip())
        if len(exc_split) > 1
        and exc_split[0].isdigit()
        and len(exc_split[0]) == 3
        else (422, str(exc))
    )
    return JSONResponse(
        status_code=status_code, content={"ok": False, "detail": msg}
    )


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"ok": False, "detail": "Internal server error"},
    )


app.include_router(router, prefix="/api")


@app.get("/", tags=["Root"])
def root():
    return {"Message": "Welcome to Environmental Impact API, see docs on /docs"}