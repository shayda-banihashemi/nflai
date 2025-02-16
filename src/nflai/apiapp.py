import requests
import json
"""import pprint
import json
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecurerequestsWarning"""

"""key = '?key=1455ced235a74c71862688fb1a38dc7f'
#https://api.sportsdata.io/v3/nfl/stats/json/ScoresFinal/2023?key=1455ced235a74c71862688fb1a38dc7f
baseURL = 'https://api.sportsdata.io/v3/nfl/stats/json/ScoresFinal/2023' + key
response_data = requests.get(baseURL)
print(response_data.status_code)"""


def getData():
    response = requests.get("https://api.sportsdata.io/v3/nfl/stats/json/ScoresFinal/2023?key=1455ced235a74c71862688fb1a38dc7f")
    print(response.status_code)
    data = json.loads(response.text)
    print(data)

getData()