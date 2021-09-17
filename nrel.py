import requests
import csv
url = "https://developer.nrel.gov/api/nsrdb/v2/solar/psm3-tmy-download.csv?api_key=DEMO_KEY"

latitude = input("Latitude: ")
longitude = input("Longitude: ")
<<<<<<< HEAD
s_Month = input("Start Month: ")
s_Day = input("Start Day: ")
s_Hour = input("Start Hour: ")
s_Min = input("Start Minute: ")
e_Month = input("End Month: ")
e_Day = input("End Day: ")
e_Hour = input("End Hour: ")
e_Min = input("End Minute: ")
list_GHI = []
#Hour = input("Hour: ")
=======
Month = input("Month: ")
Day = input("Day: ")
Hour = input("Hour: ")
>>>>>>> 92bc6265f34390867a45136d3009b1f5c03c78d6
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
<<<<<<< HEAD
        if line['Month'] == s_Month and line['Day'] == s_Day and line['Hour'] == str(int(s_Hour)-1) and line['Minute'] == s_Min:
            for line in csv_reader: 
                print("-----------------------------------")
                print("Month: " + line['Month'])
                print("Day: " + line['Day']) 
                print("Hour: " + line['Hour'])
                print("Minute: " + line['Minute'])
                print(" GHI: " + line['GHI']) 
                list_GHI.append(line['GHI'])
                if line['Month'] == e_Month and line['Day'] == e_Day and line['Hour'] == e_Hour and line['Minute'] == e_Min:
                    break
                    
    
for val in list_GHI:
    print(val)
                    
=======
        if line['Month'] == Month and line['Day'] == Day and line['Hour'] == Hour:
            print("-----------------------------------")
            print("Temperature: " + line['Temperature']) 
            print("GHI: " + line['GHI']) 
            
>>>>>>> 92bc6265f34390867a45136d3009b1f5c03c78d6





