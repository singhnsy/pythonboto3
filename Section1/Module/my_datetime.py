#Handling dates and times is made easier with this module.
from datetime import datetime

# Get current date and time
now = datetime.now()

print(now)

# Format it: %Y=Year, %m=Month, %d=Day, %H=Hour, %M=Minute
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")

print(f"Current date and time: {formatted_now}")
