import requests

response = requests.post(
    "http://localhost:5000/predict",
    json={"password": "password"},
    headers={"Content-Type": "application/json"}
)

print(response.json())