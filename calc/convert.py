import math


def mph_to_mins_per_mile(mph):
    minutes = math.floor((60/ mph))
    seconds = round((60/mph - minutes) * 60)
    time_in_seconds = minutes_to_seconds(minutes, seconds)
    return time_in_seconds

def minutes_to_seconds(minutes, seconds):
    seconds = seconds + (minutes * 60)
    return seconds

def seconds_formatter(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    mph_time: str = ("%d:%02d:%02d" % (hour, minutes, seconds))
    print(mph_time)
    return mph_time
