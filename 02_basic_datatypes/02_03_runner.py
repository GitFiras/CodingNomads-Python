'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''

# Runner's average speed in km / h
# distance from mile to km  =  10 mile * 1.6 km
# duration = 3 min 30 sec. Duration per hour = duration / seconds per hour.
# Duration in sec = 30 min * 60 sec + 30 sec = 1830 sec
# Duration per hour =  1830 / 3600
distance_km = 10 * 1.6
hours = 1830 / 3600
print("Average speed of runner over 10 miles in 30 min and 30 sec in km per hour is:")
print(distance_km / hours)