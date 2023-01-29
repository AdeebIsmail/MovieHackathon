import requests as requests

response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={31.23}&longitude={54.91}&hourly=temperature_2m")
print(response)