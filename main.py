import uvicorn
from fastapi import FastAPI

app = FastAPI()



@app.get('/', tags=["test"])
def greet():
    return {"hello": "World"}









if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
    
    