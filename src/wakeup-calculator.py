"""
    The response has to have time & minutes in military time, cos that is what cron wants.

    7:00AM
"""

from datetime import timedelta
from datetime import datetime

# don't wake up before 6:45
MIN_WAKEUP = "6:45 AM"
# or after 7:15
MAX_WAKEUP = "7:15 AM"


# for 7 sleep cycles, it should be 10 hours 30 minutes
def calculate_wakeup_time():
    now_now = datetime.now()
    wakeup_time = now_now + timedelta(hours=10, minutes=30)
    print (wakeup_time)
    return wakeup_time


# find out if waking up before 6 or after 7, ideal wake up range is 6:45 to 7:15
def is_wakeup_time_in_safe_range(wakeup_time):
    datetime_min = datetime(wakeup_time.year, wakeup_time.month, wakeup_time.day, 6, 45, 0, 0)
    datetime_max = datetime(wakeup_time.year, wakeup_time.month, wakeup_time.day, 7, 15, 0, 0)

    print(datetime_min)
    print(datetime_max)

    if datetime_min > wakeup_time > datetime_max:
        return True
    else:
        return False


"""
Put a booster song around 8:00 am to let the kids know it is time to move out.
"""


def booster_song_registration():
    print ("Bla bla ")


print (is_wakeup_time_in_safe_range(calculate_wakeup_time()))
