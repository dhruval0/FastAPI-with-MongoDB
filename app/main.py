import os
import uvicorn

if __name__ == "__main__":
    uvicorn.run("server.app:app", port=3389, lifespan="on")
