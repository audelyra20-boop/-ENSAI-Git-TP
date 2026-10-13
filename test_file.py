
import requests

url = "https://bdx.mecatran.com/utw/ws/gbfs/bordeaux/v3/station_status.json?apiKey=opendata-bordeaux-metropole-flux-gtfs-rt"

response = requests.get(url, timeout=10)
response.raise_for_status()

data = response.json()

print("Dernière mise à jour :", data["last_updated"])

for station in data["data"]["stations"][:5]:
    print(
        station["station_id"],
        station.get("num_vehicles_available"),
        station.get("num_docks_available"),
    )


