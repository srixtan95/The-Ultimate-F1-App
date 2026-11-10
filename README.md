# F1 Race Predictor

A beginner-friendly data science project that predicts Formula 1 race outcomes using Python and machine learning.

> **Status:** Work in progress. Data collection is working. Cleaning, models and the app are not built yet.

## What this project does

The goal is to predict which drivers finish on the podium, using only information known **before the race starts**: grid position, qualifying, recent form, circuit history and weather.

## Data sources

- [Jolpica-F1 API](https://github.com/jolpica/jolpica-f1): race results, qualifying and pit stops (free, no login)
- Weather data: planned (free historical weather service)

## Project structure

```
f1predictor/
├── data/
│   └── raw/          # Downloaded data (CSV files)
├── notebooks/        # Jupyter notebooks (data download, cleaning, models)
├── src/              # Reusable Python code (coming soon)
└── app/              # Streamlit app (coming soon)
```

## How to run the notebooks

1. Install Python 3.10 or newer.
2. Clone the project and open the folder:

   ```bash
   git clone https://github.com/srixtan95/f1predictor.git
   cd f1predictor
   ```

3. Create and activate a virtual environment (Windows PowerShell):

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

4. Install the libraries:

   ```bash
   pip install pandas numpy matplotlib requests ipykernel
   ```

5. Open the notebooks in VS Code and run the cells from the top.

A `requirements.txt` file will be added later.

## Disclaimer

This project is for learning only. Predictions are not betting advice. Formula 1 is not connected to this project.

## MORE FEATURES COMING SOON