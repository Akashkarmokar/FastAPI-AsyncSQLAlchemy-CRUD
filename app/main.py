from fastapi import FastAPI
from routes import init_routes
import uvicorn

app = FastAPI()

@app.get('/')
async def health_check():
    return {
        "message": "Server is started Successfully !!"
    }
init_routes(app=app)


if __name__ == "__main__":
    uvicorn.run(app=app)
