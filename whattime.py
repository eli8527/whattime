import time
import ntplib
import systime
import random

def getUnixTime(pool="time.apple.com"):
    """queries ntp time and returns actual unix time"""
    time_offset = ntplib.NTPClient().request(pool).offset
    return float(time.time()+time_offset)

if __name__ == '__main__':
    # random time - normal distribution with 5 min std
    print getUnixTime()
    rand_time = random.gauss(getUnixTime(), 300)
    systime.set_time(rand_time, 0)
