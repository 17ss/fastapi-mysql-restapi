from fastapi import FastAPI
from routes.user import user
import uvicorn

app = FastAPI()
app.include_router(user)


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')