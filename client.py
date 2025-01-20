import requests

# Define the server address, using the Tailscale IP of the server
url = "http://100.69.203.85:8000"

# Data to send to the server
data = {"message": "Hello, server!"}

try:
    # Make a POST request to the server
    response = requests.post(url, json=data)

    # Print the response from the server
    print(f"Server responded with: {response.status_code} - {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Error communicating with the server: {e}")
