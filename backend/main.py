from fastapi import FastAPI

app = FastAPI(title="F1 Predictor API")


@app.get("/")
def home():
    return {"message": "F1 predictor backend is running"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}


from fastapi import FastAPI, HTTPException

from f1predictor.data import get_schedule

app = FastAPI(title="F1 Predictor API")


@app.get("/")
def home():
    return {"message": "F1 predictor backend is running"}


@app.get("/schedule/{year}")
def schedule(year: int):
    if year < 1950 or year > 2100:
        raise HTTPException(status_code=400, detail="Year must be between 1950 and 2100")

    table = get_schedule(year)
    if table.empty:
        raise HTTPException(status_code=404, detail=f"No races found for {year}")

    return table.to_dict(orient="records")