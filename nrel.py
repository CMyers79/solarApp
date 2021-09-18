import requests
import csv
url = "https://developer.nrel.gov/api/nsrdb/v2/solar/psm3-tmy-download.csv?api_key=DEMO_KEY"
list_GHI = []
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
}
""" coord[0] = latitude
coord[1] = longitude
s_Date[0] = s_Month
s_Date[1] = s_Day
s_Date[2] = s_Hour
s_Date[3] = s_Min
e_Date[0] = e_Month
e_Date[1] = e_Day
e_Date[2] = e_Hour
e_Date[3] = e_Min """
def get_GHI(coord, s_Date, e_Date):
    payload = "wkt=POINT("+str(coord[0])+"%20"+str(coord[1])+")&attributes=dhi%2Cdni%2Cghi%2Cdew_point%2Cair_temperature%2Csurface_pressure%2Cwind_direction%2Cwind_speed%2Csurface_albedo%2C%2C%2C&names=tmy-2020&full_name=Dongwoo%Kang&email=kangdo@oregonstate.edu&affiliation=OregonStateUniversity&mailing_list=false&reason=test&utc=true"
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response)
    file1 = open("corvallis.csv","w")
    file1.write(response.text)
    with open('corvallis.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        csv_reader.fieldnames = "Year" ,"Month","Day","Hour","Minute","DHI","DNI","GHI","Dew Point","Temperature","Pressure","Wind Direction","Wind Speed","Surface Albedo"
        for line in csv_reader:
            if line['Month'] == s_Date[0] and line['Day'] == s_Date[1] and line['Hour'] == str(int(s_Date[2])-1) and line['Minute'] == s_Date[3]:
                for line in csv_reader: 
                    list_GHI.append(line['GHI'])
                    if line['Month'] == e_Date[0] and line['Day'] == e_Date[1] and line['Hour'] == str(int(s_Date[2])-1) and line['Minute'] == s_Date[3]:
                        break
    return list_GHI

#get_GHI(latitude = "44",longitude = "-123", s_Month = "1", s_Day = "1", s_Hour = "14", s_Min = "30", e_Month = "1", e_Day = "1", e_Hour = "16", e_Min = "30")
""" for val in list_GHI:
    print(val) """





