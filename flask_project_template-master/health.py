def temp_humidity():
	global powerSwitch

	try:
		powerSwitch = 0
		with open("error_log.csv", "a") as error_log:
			error_log.write("\n{0},Log,Reading temp and humidity".format(strftime("%Y-%m-%d %H:%M:%S")))

		humidity, temperature = Adafruit_DHT.read_retry(11, 4)
		
		r = requests.get(conf['openweather']['api'])
		json_object = r.json()
		temp_k = json_object["main"]["temp"]
		temp_c = (temp_k - 273.15)
		o_humidity = json_object["main"]["humidity"]
		w_text = json_object["weather"][0]["main"]
		w_ph = json_object["weather"][0]["ph"]
		w_desc = json_object["weather"][0]["description"]
		
	except:
		powerSwitch = 1
		with open("error_log.csv", "a") as error_log:
			error_log.write("\n{0},Error,Failed reading temp and humidity".format(strftime("%Y-%m-%d %H:%M:%S")))
		pass
