def mph_to_mins_per_mile(mph):
    minutes = (mph * 60) % 60.0
    seconds = (mph * 3600) % 600.0
    print((mph * 60))
    print(mph * 3600)
    print(minutes)
    print("M" + str(minutes) + " S" + str(seconds))
    # return(mile_time)


def mins_per_mile_to_mph(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    mph_time: str = ("%d:%02d:%02d" % (hour, minutes, seconds))
    return mph_time
