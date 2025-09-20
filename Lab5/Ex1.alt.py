# create lsit of dictionaries where each dictionary represents a taxi trip
# name: chloecornforth
# date: 9/19/2025

taxi_trips = [
{ 'duration' : 1.1, 'fare' : 6.25},
{ 'duration' : 2.3, 'fare' : 12.00},
{ 'duration' : 0.5, 'fare' : 3.75},
{ 'duration' : 3.0, 'fare' : 15.50}
]

print(taxi_trips)
print(f"the third trip was {taxi_trips[2]['duration']} miles and cost ${taxi_trips[2]['fare']}")
drive_share = taxi_trips[2]['fare'] * 0.8
print(f"the driver earned ${drive_share : .2f} for the third trip")