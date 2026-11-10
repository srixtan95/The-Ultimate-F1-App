"""Download Formula 1 data from the Jolpica API."""

import time

import pandas as pd
import requests

BASE_URL = "https://api.jolpi.ca/ergast/f1"


def get_race_results(year, round_number):
    """Return the results of one race as a DataFrame.

    Return an empty DataFrame if the race does not exist.
    """
    url = f"{BASE_URL}/{year}/{round_number}/results.json"
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    races = response.json()["MRData"]["RaceTable"]["Races"]
    if len(races) == 0:
        return pd.DataFrame()

    race = races[0]
    rows = []
    for result in race["Results"]:
        rows.append({
            "year": int(race["season"]),
            "round": int(race["round"]),
            "circuit": race["Circuit"]["circuitId"],
            "date": race["date"],
            "driver": result["Driver"]["driverId"],
            "team": result["Constructor"]["constructorId"],
            "grid": int(result["grid"]),
            "position": int(result["position"]),
            "status": result["status"],
        })

    return pd.DataFrame(rows)


def get_season_results(year, pause=0.5):
    """Return the results of every race in one season."""
    tables = []
    for round_number in range(1, 31):
        table = get_race_results(year, round_number)
        if table.empty:
            break
        tables.append(table)
        time.sleep(pause)

    if not tables:
        return pd.DataFrame()
    return pd.concat(tables, ignore_index=True)

def get_schedule(year):
    """Return the race calendar of one season as a DataFrame."""
    url = f"{BASE_URL}/{year}.json"
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    races = response.json()["MRData"]["RaceTable"]["Races"]

    rows = []
    for race in races:
        rows.append({
            "round": int(race["round"]),
            "name": race["raceName"],
            "circuit": race["Circuit"]["circuitName"],
            "country": race["Circuit"]["Location"]["country"],
            "date": race["date"],
        })

    return pd.DataFrame(rows)