from datetime import datetime
from zoneinfo import ZoneInfo

locations = {
    "India - Bengaluru": "Asia/Kolkata",
    "USA - New York": "America/New_York",
    "UK - London": "Europe/London",
    "Japan - Tokyo": "Asia/Tokyo",
    "Australia - Sydney": "Australia/Sydney"
}

print("===== WORLD TIME =====")

for city, timezone in locations.items():
    current_time = datetime.now(ZoneInfo(timezone))
    print(city, ":", current_time.strftime("%d-%m-%Y %I:%M:%S %p"))
  
