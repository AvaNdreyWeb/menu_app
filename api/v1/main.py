from fastapi import FastAPI

BASE_PATH = '/api/v1'

app = FastAPI()


@app.get(BASE_PATH)
def hello():
    return {"code": 200, 'msg': 'OK'}
