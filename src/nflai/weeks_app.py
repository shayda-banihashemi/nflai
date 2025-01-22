import os
import json
import pprint

def weeks_gather_data():
    directory = "data/weeks/"
    weeks_docs = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            print(file)
            with open(f"{directory}{file}", encoding='utf-8', errors='ignore') as f:
                data = f.read()
            raw_data = json.loads(data)
            for game in raw_data:
                if game['HomeScore'] > game['AwayScore']:
                    weeks_docs.append(f"The home team {game['HomeTeam']} won against the away team {game['AwayTeam']} by "
                                      f"{game['HomeScore'] - game['AwayScore']} points on {
                                          game['StadiumDetails']['PlayingSurface']} "
                                      f"{game['StadiumDetails']['Type']}")
                else:
                    weeks_docs.append(f"The away team {game['AwayTeam']} won against the home team {game['HomeTeam']} by "
                                      f"{game['AwayScore'] - game['HomeScore']} points")
    return weeks_docs


if __name__ == "__main__":
    weeks = weeks_gather_data()
    pprint.pprint(weeks)
