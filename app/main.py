import asyncio
from fastapi import FastAPI
import uvicorn

from users.router import router as router_users
app = FastAPI()

app.include_router(router_users)

# loop = asyncio.get_event_loop()
# KAFKA_INSTANCE = "localhost:29092"


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)