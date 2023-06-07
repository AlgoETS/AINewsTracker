from fastapi import FastAPI

# import all routers
from .routers import users
from .routers import companies

# init app
app = FastAPI()

# add all routers to app
app.include_router(users.router)
app.include_router(companies.router)


# this is command to run the server : uvicorn app.main:app --reload~
@app.get("/")
async def root():
    return 'AI News Tracker API'
