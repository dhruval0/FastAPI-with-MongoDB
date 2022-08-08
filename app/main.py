import os
import uvicorn

if __name__ == "__main__":
    uvicorn.run("server.app:app", port=7777, lifespan="on")
