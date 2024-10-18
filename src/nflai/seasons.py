import os
import json

def gather_data():
    directory = "/Users/shaydabanihashemi/ws/nflai/data/seasons/"
    processed_data = []
    for file in os.listdir(directory):
        with open(os.path.join(directory, file)) as f:
            data = f.read()
            raw_data = json.loads(data)

    for team in raw_data:
        processed_data.append(f"The {team['Name']} belong to the {team['Conference']} Conference.")
        processed_data.append(f"The {team['Name']} belong to the {team['Conference']} {team['Division']}")
        processed_data.append(f"The {team['Name']} won {team['Wins']} games")
        processed_data.append(f"The {team['Name']} lost {team['Losses']} games")
        processed_data.append(f"The {team['Name']} win {(team['Percentage'])*100}% of the time")
        processed_data.append(f"The {team['Name']} scored {team['PointsFor']} points")
        processed_data.append(f"The {team['Name']} won {team['DivisionWins']} division games")
        processed_data.append(f"The {team['Name']} lost {team['DivisionLosses']} division games")
        processed_data.append(f"The {team['Name']} won {team['ConferenceWins']} conference games")
        processed_data.append(f"The {team['Name']} lost {team['ConferenceLosses']} conference games")
        processed_data.append(f"The {team['Name']} rank {team['GlobalTeamID']} in the NFL")
        processed_data.append(f"The {team['Name']} rank {team['DivisionRank']} in the division")
        processed_data.append(f"The {team['Name']} rank {team['ConferenceRank']} in the conference")
        processed_data.append(f"The {team['Name']} won {team['HomeWins']} home games")
        processed_data.append(f"The {team['Name']} lost {team['HomeLosses']} home games")
        processed_data.append(f"The {team['Name']} won {team['AwayWins']} away games")
        processed_data.append(f"The {team['Name']} lost {team['AwayLosses']} away games")
        processed_data.append(f"The {team['Name']} has a win streak of {team['Streak']} games")
    return processed_data
