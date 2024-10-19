#This program calculates distance between 2 sites author: Yash Pednekar 

from math import cos, asin, sqrt, pi
import csv

def distance(lat1, lon1, lat2, lon2):
    r = 6371 # km
    p = pi / 180

    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 2 * r * asin(sqrt(a))


# File paths
file_path = 'sites.csv'
file_path2 = 'sites_distance.csv'

# Read the CSV file
with open(file_path, mode='r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    # Storing the content as a list of dictionaries
    records = [row for row in reader]

# Calculate distances and write results to a new CSV file
with open(file_path2, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(['cell_id_1','Lat1', 'Lon1', 'cell_id_2', 'Lat2', 'Lon2','distance_km'])
    
    # Re-running the distance calculation logic
    for i in range(len(records)):
        for j in range(i + 1, len(records)):
            cell1 = records[i]['cell_id']
            cell2 = records[j]['cell_id']
            lat1, lon1 = float(records[i]['Lat']), float(records[i]['Long'])
            lat2, lon2 = float(records[j]['Lat']), float(records[j]['Long'])
            
            # Calculate the distance between the two cell locations
            dist = distance(lat1, lon1, lat2, lon2)
            
            # Write the calculated distance to the output file
            if dist < 2:
              writer.writerow([cell1, lat1, lon1, cell2, lat2,lon2,round(dist, 2)])  # Rounded to 2 decimal places

