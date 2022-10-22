import fastapi
import uvicorn
import os
import json
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title='Indonesian Formalizer')

class inputData(BaseModel):
    data: list

@app.get("/")
async def root():
    return {"message": "System Online!"}

@app.get('/results')
async def getResult():
    path = 'output/supervised/evaluation/predict.for'
    if(os.path.exists(path)):
        with open(path) as f:
            lines = f.read().splitlines()
        message = {'data':lines}
        return message
    else:
        path = 'data/labelled/test.inf'
        if(not os.path.exists(path)):
            return {'error':'tidak ada data uji!'}
        else:
            return {'warning':'proses formalisasi sedang berlangsung.'}

@app.post('/insert_data')
async def postData(data: inputData):
    text = data.dict()['data']
    path = 'data/labelled/test.inf'
    with open(path, 'w') as f:
        for line in text:
            f.write(f"{line}\n")
    return {'info':'Mulai proses pelatihan dan pengujian!'}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001)