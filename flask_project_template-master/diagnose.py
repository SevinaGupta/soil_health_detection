def self_diagnostics():
	led_off()
	
	global powerSwitch
	global ledSwitch
	
	ledSwitch = 1
	
	Thread(target = led_rolling).start()
	
	try:
		powerSwitch = 0
		with open("error_log.csv", "a") as error_log:
			error_log.write("\n{0},Log,Diagnostics start up sequence".format(strftime("%Y-%m-%d %H:%M:%S")))
		tts = gTTS(text="Alert. Empire plant pot online. Self diagnostics start up sequence initiated. Checking ligths." , lang='en')
		tts.save("diagnostics_lights.mp3")
		os.system("mpg321 -q diagnostics_lights.mp3")
	except:
		powerSwitch = 1
		with open("error_log.csv", "a") as error_log:
			error_log.write("Error: Internet error.".format(strftime("%Y-%m-%d %H:%M:%S")))
		os.system("mpg321 -q diagnostics_lights_backup.mp3")
		pass
	
	ledSwitch = 0
	time.sleep(2)
	led_all_on()
	time.sleep(1)
	led_blue()
	time.sleep(1)
	led_green()
	time.sleep(1)
	led_red()
	time.sleep(1)
	led_off()
	ledSwitch = 1
	
	Thread(target = led_rolling).start()
	
	humidity, temperature = Adafruit_DHT.read_retry(11, 4)
	temp = cpu.temperature
	
	try:
		powerSwitch = 0
		tts = gTTS(text="Self diagnostics. Central core CPU runs at {0:0.0f} degrees celsius. Room temperature is {1:0.0f} degrees celsius with a relative humidity of {2:0.0f} percent.".format(temp, temperature, humidity) , lang='en')
		tts.save("diagnostics.mp3")
		os.system("mpg321 -q diagnostics.mp3")
	except:
		powerSwitch = 1
		os.system("mpg321 -q diagnostics_backup.mp3")
		pass
	
	ledSwitch = 0
	time.sleep(2)
	internet_on()
