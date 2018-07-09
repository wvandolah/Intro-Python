# Make an array of dictionaries. Each dictionary should have keys:
#
# lat: the latitude
# lon: the longitude
# name: the waypoint name
#
# Make up three entries of various values.

waypoints = [
  {'lat': 1235,
  'lon': 5321,
  'name':'not a place'},
  {'lat': 5522,
  'lon': 9975,
  'name':'also not a place'},
  {'lat': 1235,
  'lon': 5321,
  'name':'not a place your mom would visit'}
  
]

# Write a loop that prints out all the field values for all the waypoints
for i in waypoints:
  print('lat:',i['lat'],'lon:',i['lon'],'name:',i['name'])