from fastapi import FastAPI
from scraper import get_prices
from datetime import datetime

app= FastAPI()

@app.get("/")
def root():
    return {"message": "Health check is good"}

@app.get("/prices")
def prices():
    return {"prices" : get_prices(),
            "updated": datetime.now()}


def get_time():
    return {"time": datetime.now()}
    

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000) 