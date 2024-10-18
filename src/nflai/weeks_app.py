import os
import json

directory = "/Users/shaydabanihashemi/ws/nflai/data/weeks/"
docs = []
for file in os.listdir(directory):
    with open(os.path.join(directory, file)) as f:
        data = f.read()
        raw_data = json.loads(data)
        """print(raw_data)
        print(type(raw_data))"""
        for game in raw_data:
            if game['HomeScore'] > game['AwayScore']:
                docs.append(f"The home team {game['HomeTeam']} won against the away team {game['AwayTeam']} by "
                            f"{game['HomeScore'] - game['AwayScore']} points on {game['StadiumDetails']['PlayingSurface']} {game['StadiumDetails']['Type']}")
            else:
                docs.append(f"The away team {game['AwayTeam']} won against the home team {game['HomeTeam']} by {game['AwayScore'] - game['HomeScore']} points")

print(docs)
print(len(docs))