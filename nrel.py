import requests
import csv

url = "https://developer.nrel.gov/api/nsrdb/v2/solar/psm3-tmy-download.csv?api_key=aCCaQK7ZmrwW3aDTi2vViUpgjBBcV1KN215VOCK4"
list_GHI = []
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
}


def get_GHI(coord, s_Date, e_Date):
    payload = "wkt=POINT("+str(coord[1])+"%20"+str(coord[0])+")&attributes=dhi%2Cdni%2Cghi%2Cdew_point%2Cair_temperature%2Csurface_pressure%2Cwind_direction%2Cwind_speed%2Csurface_albedo%2C%2C%2C&names=tmy-2020&full_name=Dongwoo%Kang&email=kangdo@oregonstate.edu&affiliation=OregonStateUniversity&mailing_list=false&reason=test&utc=false"
    response = requests.request("POST", url, data=payload, headers=headers)

    file1 = open("corvallis.csv","w")
    file1.write(response.text)
    with open('corvallis.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        csv_reader.fieldnames = "Year", "Month", "Day", "Hour", "Minute", "DHI", "DNI", "GHI", "Dew Point", "Temperature", "Pressure", "Wind Direction", "Wind Speed", "Surface Albedo"
        for line in csv_reader:
            if line['Month'] == str(s_Date[0]) and line['Day'] == str(s_Date[1]) and line['Hour'] == str(int(s_Date[2]) - 1):
                for line in csv_reader: 
                    list_GHI.append(line['GHI'])
                    if line['Month'] == str(e_Date[0]) and line['Day'] == str(e_Date[1]) and line['Hour'] == str(int(e_Date[2]) - 1):
                        break
    return list_GHI
