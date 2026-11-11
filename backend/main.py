from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles

from f1predictor.data import get_schedule

app = FastAPI(title="F1 Predictor API")

FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"


@app.get("/api/health")
def health():
    return {"message": "F1 predictor backend is running"}


@app.get("/api/schedule/{year}")
def schedule(year: int):
    if year < 1950 or year > 2100:
        raise HTTPException(status_code=400, detail="Year must be between 1950 and 2100")

    table = get_schedule(year)
    if table.empty:
        raise HTTPException(status_code=404, detail=f"No races found for {year}")

    return table.to_dict(orient="records")


# This line must stay LAST. It serves the files in the frontend folder.
app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")