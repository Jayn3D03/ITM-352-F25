# zip together a list of trip durations and a tuple of trip fares
# from this zip we're going to create a dictionary
# name: chloecornforth
# date: 9/24/2025

trip_durations = [1.1, 0.8, 2.5, 2.6]
trip_fares = (6.25, 5.25, 10.50, 8.05)

trips = dict(zip(trip_durations, trip_fares))
print(trips)

trips_num = int(input("what trip do you want? : "))
print(f"duration: {list(trips.keys())[trips_num - 1]} miles")
print(f"cost: ${list(trips.values())[trips_num - 1]:.2f}")