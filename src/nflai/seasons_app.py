import os
import json
import requests
import pandas as pd

def getDataFrame():
    response = requests.get("https://api.sportsdata.io/v3/nfl/scores/json/Standings/2023?key=1455ced235a74c71862688fb1a38dc7f")
    print(response.status_code)
    data = json.loads(response.text)
    df = pd.DataFrame(data)
    return df

def seasons_gather_data(data_frame):
    season_docs = []
    for team in data_frame.itertuples():
        season_docs.append(f"The {team.Name} belong to the {team.Conference} Conference.")
        season_docs.append(f"The {team.Name} belong to the {team.Conference} {team.Division}")
        season_docs.append(f"The {team.Name} won {team.Wins} games")
        season_docs.append(f"The {team.Name} lost {team.Losses} games")
        season_docs.append(f"The {team.Name} win {(team.Percentage)*100}% of the time")
        season_docs.append(f"The {team.Name} scored {team.PointsFor} points")
        season_docs.append(f"The {team.Name} won {team.DivisionWins} division games")
        season_docs.append(f"The {team.Name} lost {team.DivisionLosses} division games")
        season_docs.append(f"The {team.Name} won {team.ConferenceWins} conference games")
        season_docs.append(f"The {team.Name} lost {team.ConferenceLosses} conference games")
        season_docs.append(f"The {team.Name} rank {team.GlobalTeamID} in the NFL")
        season_docs.append(f"The {team.Name} rank {team.DivisionRank} in the division")
        season_docs.append(f"The {team.Name} rank {team.ConferenceRank} in the conference")
        season_docs.append(f"The {team.Name} won {team.HomeWins} home games")
        season_docs.append(f"The {team.Name} lost {team.HomeLosses} home games")
        season_docs.append(f"The {team.Name} won {team.AwayWins} away games")
        season_docs.append(f"The {team.Name} lost {team.AwayLosses} away games")
        season_docs.append(f"The {team.Name} has a win streak of {team.Streak} games")
        season_docs.append(f"The {team.Name} is the acronym for {team.Name}")
    print(season_docs)
    return season_docs

if __name__ == "__main__":
    data = seasons_gather_data(getDataFrame())
