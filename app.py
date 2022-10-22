import fastapi
import uvicorn
from fastapi import FastAPI


app = FastAPI(title='Indonesian Formalizer')

@app.get("/")
async def root():
    return {"message": "System Online!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001)