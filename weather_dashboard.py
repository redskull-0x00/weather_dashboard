import matplotlib.pyplot as plt
import requests
from datetime import datetime
from dotenv import load_dotenv
import os


try:
    load_dotenv()
except ImportError:
    print("python-dotenv is not installed.Using direct key input")

# Option 1 : Loading API key from .env (recommended)
API_KEY = os.getenv("API_KEY")
# Option 2 : if no .env,enter your API here
if not API_KEY:
    API_KEY = ""#Enter API key 

if not API_KEY:
    raise ValueError("Please provide an API key in .env or directly in the script.")    

CITY = "London" #Change City 
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

#Fetching weather 
response = requests.get(URL)
response.raise_for_status()
data =response.json()
#Extracting time and temperature 
temps = [forecast["main"]["temp"]  for forecast in data["list"][:8]] #24 Hours(3-Hour intervals [8x3=24])
times = [datetime.fromtimestamp(forecast["dt"]).strftime("%H:%M") for forecast in data["list"][:8]]

#Creating plot
plt.figure(figsize=(10, 6), facecolor='lightblue')
plt.plot(times,temps,color="red",marker="o",linewidth=2,markersize=8)
plt.title("Weather",fontsize=14)
plt.xlabel("Time",fontsize=12,)
plt.ylabel("Temperature (°C)", fontsize=12,)
plt.grid(True, linestyle="--", alpha=0.7) 
plt.show()

print(f"Current Temperature in {CITY}:{temps[0]} Celsius")