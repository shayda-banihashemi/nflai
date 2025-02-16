import os
import requests
import json
import pandas as pd

def getDataFrame():
    response = requests.get("https://api.sportsdata.io/v3/nfl/stats/json/ScoresFinal/2023?key=1455ced235a74c71862688fb1a38dc7f")
    print(response.status_code)
    data = json.loads(response.text)
    df = pd.DataFrame(data)
    return df

def weeks_gather_data(data_frame):
    weeks_docs = []
    for row in data_frame.itertuples():
        if row.HomeScore > row.AwayScore:
            weeks_docs.append(f"The home team {row.HomeTeam} won against the away team {row.AwayTeam} by "
                              f"{row.HomeScore - row.AwayScore} points.")
        else:
            weeks_docs.append(f"The away team {row.AwayTeam} won against the home team {row.HomeTeam} by "
                              f"{row.AwayScore - row.HomeScore} points")
    return weeks_docs

if __name__ == "__main__":
    var = weeks_gather_data(getDataFrame())