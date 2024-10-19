from math import cos, asin, sqrt, pi
import csv

def distance(lat1, lon1, lat2, lon2):
    r = 6371 # km
    p = pi / 180

    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 2 * r * asin(sqrt(a))

print("distance = ")
print(distance(51.539475,-0.022061111,54.53843056,-6.080183333))

# Initialize an empty list to store the data
data = []
converted_data = []

# Open the CSV file
with open('sites.csv', mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Append each row to the data list
        data.append(row)

# Print the data to verify
print(data)
with open('sites_with_distances.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

# Writing each row
    writer.writerows(data)


