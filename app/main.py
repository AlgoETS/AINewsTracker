from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from fastapi_cache.decorator import cache
from fastapi_health import health
import uvicorn
from prometheus_fastapi_instrumentator import Instrumentator


# import all routers
from .routers import users
from .routers import company

swagger_ui_parameters = {
    "dom_id": "#swagger-ui",
    "layout": "BaseLayout",
    "deepLinking": True,
    "showExtensions": True,
    "showCommonExtensions": True,
    "syntaxHighlight.theme": "obsidian",
}

# init app
app = FastAPI(
    title="AI News Tracker API",
    description="AI News Tracker API",
    version="0.0.1",
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/v1/docs",
    swagger_ui_parameters=swagger_ui_parameters,
    redoc_url=None,
)

# add all routers to app
app.include_router(users.router)
app.include_router(company.router)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# add cache middleware to app
@cache()
async def get_cache() -> int:
    """Get cache TTL from config.
    Returns:
        int: Cache TTL
    """
    return 1

@app.on_event("startup")
async def startup():
    # redis = init_redis_pool("localhost", "")
    # FastAPICache.init(backend=RedisBackend(redis), prefix="fastapi-cache")
    FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")


def healthy():
    # get basic metric about fastapi app
    return True

def sick():
    return False

@app.get("/health", tags=["Health"])
def read_health():
    if health([healthy, sick]):
        return {
        "status": "ok",
        "version": "0.1.0",
        "uptime": 10,
        "hostname": "localhost",
        "environment": "dev",
        "dependencies": {
            "redis": {
                "status": "ok",
                "version": "6.0.9",
                "uptime": 10,
                "hostname": "localhost",
                "environment": "dev",
            },
            "mongodb": {
                "status": "ok",
                "version": "4.4.6",
                "uptime": 10,
                "hostname": "localhost",
                "environment": "dev",
            },
            "prometheus": {
                "status": "ok",
                "version": "2.26.0",
                "uptime": 10,
                "hostname": "localhost",
                "environment": "dev",
            },
        },
    }
    return {"status": "sick"}


# this is command to run the server : uvicorn app.main:app --reload~
@app.get("/", tags=["Root"])
@cache(expire=60)
def read_root():
    return "AI News Tracker API"


def start(host: str = "0.0.0.0", port: int = 8000,reload: bool = True):
    """Launched with `poetry run start` at root level"""
    uvicorn.run("app.app:app", host=host, port=port, reload=reload, workers=2)

if __name__ == "__main__":
    Instrumentator().instrument(app).expose(app)
    start()