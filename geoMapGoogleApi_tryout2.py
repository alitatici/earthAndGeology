import googlemaps
import pandas

gmaps_key = googlemaps.Client(key="Google API Key")

dataFrame = pandas.read_csv('GoogleAPI_Adressess.csv')
dataFrame["LAT"] = None
dataFrame["LON"] = None

for i in range(0, len(dataFrame)):
    
    geocode_result = gmaps_key.geocode(dataFrame.iat[i,0])
    
    lat = geocode_result[0]["geometry"]["location"]["lat"]
    lng = geocode_result[0]["geometry"]["location"]["lng"]
    dataFrame.iat[i, dataFrame.columns.get_loc("LAT")] = lat
    dataFrame.iat[i, dataFrame.columns.get_loc("LON")] = lng
    print(lat,lng)
    
