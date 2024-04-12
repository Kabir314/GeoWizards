import requests
from dotenv import dotenv_values
import os

env_path = f"{os.getcwd()}\\.env"
config = dotenv_values(env_path)
print(config)

def get_route_details(
        starting_lat,
        starting_long,
        dest_lat,
        dest_long,
        transport_mode = "car",
        api_key = config["here_api_key"]
):
    params = {
        "transportMode" : transport_mode,
        "origin" : f"{starting_lat},{starting_long}",
        "destination" : f"{dest_lat},{dest_long}",
        "return" : "travelSummary",
        "apikey" : api_key
    }
    response = requests.get("https://router.hereapi.com/v8/routes", params = params)
    print(response.url)
    #First route, we are interested in only part of the response
    dict = response.json()["routes"][0]["sections"][0]
    return {
        "route_duration_seconds" : dict["travelSummary"]["duration"],
        "length_meters" : dict["travelSummary"]["length"]
    }

#Test
output = get_route_details(
    starting_lat = 52.5307999,
    starting_long = 13.3847,
    dest_lat = 52.5323264,
    dest_long = 13.378874
)
print(output)
