import convert
usr_entered_time = float(input("Enter Run Time in MPH: "))
mile_time = convert.run(usr_entered_time)
print("Minutes Per Mile: " + mile_time)
