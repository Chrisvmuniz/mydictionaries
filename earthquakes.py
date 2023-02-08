'''
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries

1) print out the number of earthquakes

2) iterate through the dictionary and extract the location, magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a 
   magnitude > 6. Print out the new dictionary.

3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

'''


import json

#Open and load file
infile = open ("eq_data.json",'r')
earthquakes = json.load(infile)

#number of earthquakes
print("===== Print Number of Total Earthquakes =====")
print(len(earthquakes["features"]))
print("\n")



#Create our new dictionary
eq_dict = {}
#We have to initialize count for our keys to be unique
count = 0
for x in earthquakes["features"]:
    #We only want Mag above 6
    if x["properties"]["mag"] > 6:
        earthquake = {'loc': x["properties"]["place"],'mag': x["properties"]["mag"],'lon':x["geometry"]["coordinates"][0],'lat':x["geometry"]["coordinates"][1]}
        eq_dict["EarthquakeNum_" + str(count)] = earthquake 
        #We increment count so our keys will be unique
        count +=1 
#print out new dictionary 
print("===== Print New Dictionary =====")
print(eq_dict)
print("\n")

#Go through our new dictionary and print out everything in format requested
print("===== Print Dictionary(Requested Format) =====")
for x in eq_dict:
    print("Location: " + str(eq_dict[x]["loc"]) + "\n" + "Magnitude: " + str(eq_dict[x]["mag"]) + "\n" + "Longitude: " + str(eq_dict[x]["lon"]) + "\n" + "Latitude: " + str(eq_dict[x]["lat"]) + "\n")

   