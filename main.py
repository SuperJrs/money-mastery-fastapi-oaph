from fastapi import FastAPI
from controllers.conta import router

app = FastAPI()

app.include_router(router)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='localhost', port=8080, reload=True)
    