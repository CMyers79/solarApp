latitude = float(input("Enter the latitude: "))

longitude = float(input("Enter the longitude: "))

coordinate = [latitude, longitude]

start_date = input("Enter the date in format 'mm/dd/hh': ")

start_date_list = start_date.split("/")

formatted_start_date = [int(start_date_list[0]), int(start_date_list[1]), int(start_date_list[2])]

print(formatted_start_date)

end_date = input("Enter the end date in format 'mm/dd/hh': ")

end_date_list = end_date.split("/")

formatted_end_date = [int(end_date_list[0]), int(end_date_list[1]), int(end_date_list[2])]

led_fixtures = int(input("Enter number of LED fixtures: "))

fluorescent_fixtures = int(input("Enter number of fluorescent fixtures: "))

lighting_watts = led_fixtures * 2.5 + fluorescent_fixtures * 10

lighting_hours = input("Enter the number of lighting hours: ")

average_plug_load_watts = input("Enter average plug load watts: ")
if average_plug_load_watts == "":
	average_plug_load_watts = 50
else:
	average_plug_load_watts = int(average_plug_load_watts)

water_usage = input("Enter total gallons: ")

watt_hours = float(water_usage) * 0.5

refrigerator = 0

mode = input("Enter fridge mode: 1 for propane, 2 for DC, 3 for AC.")
if mode == 1:
	refrigerator = 15
elif mode == 2:
	refrigerator = 220
elif mode == 3:
	refrigerator = 275
