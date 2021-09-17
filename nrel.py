import requests
import csv
url = "https://developer.nrel.gov/api/nsrdb/v2/solar/psm3-tmy-download.csv?api_key=DEMO_KEY"

latitude = input("Latitude: ")
longitude = input("Longitude: ")
Month = input("Month: ")
Day = input("Day: ")
Hour = input("Hour: ")
payload = "wkt=POINT("+longitude+"%20"+latitude+")&attributes=dhi%2Cdni%2Cghi%2Cdew_point%2Cair_temperature%2Csurface_pressure%2Cwind_direction%2Cwind_speed%2Csurface_albedo%2C%2C%2C&names=tmy-2020&full_name=Dongwoo%Kang&email=kangdo@oregonstate.edu&affiliation=OregonStateUniversity&mailing_list=false&reason=test&utc=true"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
}

response = requests.request("POST", url, data=payload, headers=headers)
#print(response.text)
file1 = open("corvallis.csv","w")
file1.write(response.text)

with open('corvallis.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    csv_reader.fieldnames = "Year" ,"Month","Day","Hour","Minute","DHI","DNI","GHI","Dew Point","Temperature","Pressure","Wind Direction","Wind Speed","Surface Albedo"
    for line in csv_reader:
        if line['Month'] == Month and line['Day'] == Day and line['Hour'] == Hour:
            print("-----------------------------------")
            print("Temperature: " + line['Temperature']) 
            print("GHI: " + line['GHI']) 
            





