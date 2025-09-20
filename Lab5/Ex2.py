# define a list of taxi trip durations in miles 
# (use values 1.1, 0.8, 2.5, 2.6). Also define a tuple of fares for the same number of trips)
# (use values “$6.25,” “$5.25,” “$10.50,” “$8.05”)
# store tuples and lists as values in a dictionary with keys 
# "trip_miles" and "trip_fares"
# name: chloecornforth
# date: 9/19/2025

trip_durations = [1.1, 0.8, 2.5, 2.6]
trip_fares = (6.25, 5.25, 10.50, 8.05)

trips = { "miles" : trip_durations,
          "fares" : trip_fares }

print(trips)
print(f"The duration of the third trip is {trips['miles'][2]} miles")
print(f"The cost of the third trip is ${trips['fares'][2]:.2f}")

trips["miles"].append(2.2)
(trips["fares"]) += (4.0,)
print(trips)

trip_num = int(input("what trip do you want? : "))
print(f"duration: {trips['miles'][trip_num - 1]} miles")
print(f"cost: ${trips['fares'][trip_num - 1]:.2f}")