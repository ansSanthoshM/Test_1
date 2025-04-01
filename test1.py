import os
import datetime
import pytz

ist = pytz.timezone('Asia/Kolkata')
timestamp_ist = datetime.datetime.now(ist).strftime("%Y%m%d%H%M%S")
print(f"Current Data & Time: {timestamp_ist}")
print("Test1")
