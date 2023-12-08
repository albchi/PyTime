from datetime import datetime

# prints local time

# harder to use, but easier to see
# 2023-12-08 02:05:33
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# easier to use, but messier to see
# 2023-12-08 02:05:33.228123
print(str(datetime.now())) 


# --- another method ---

from datetime import datetime # needed for datetime.now
from pytz import timezone # needed for timezone

format = "%Y-%m-%d %H:%M:%S %Z%z"

zone_name = 'US/Pacific'
print(f"Time in {zone_name} is")
pst_zone = datetime.now(timezone(zone_name))
print(pst_zone.strftime(format))

zone_name = 'Asia/Seoul'
print(f"Time in {zone_name} is")
kor_zone = datetime.now(timezone(zone_name))
print(kor_zone.strftime(format))

# ---- not fun ---
#import time
# seconds passed since epoch
# seconds = 1672215379.5045543
#seconds = 1972215379.5045543

# convert the time in seconds since the epoch to a readable format
#local_time = time.ctime(seconds)
#print("Local time:", local_time)
