def internet_on():
	with open("error_log.csv", "a") as error_log:
		error_log.write("\n{0},Log,Testing Internet connection.".format(strftime("%Y-%m-%d %H:%M:%S")))
	
	global ledSwitch
	global connected
	global powerSwitch
	
	try:
		powerSwitch = 0
		urllib.request.urlopen('http://216.58.207.206')
		#urllib.urlopen('http://216.58.207.206', timeout=4)

		with open("error_log.csv", "a") as error_log:
			error_log.write("\n{0},Log,We have an internet connection.".format(strftime("%Y-%m-%d %H:%M:%S")))
		
		ledSwitch = 1
		
		Thread(target = led_green_alert).start()
		
		try:
			powerSwitch = 0
			tts = gTTS(text="Code green! All communication systems are online and working within normal parameters." , lang='en')
			tts.save("internet_on.mp3")
			os.system("mpg321 -q internet_on.mp3")
		except:
			powerSwitch = 1
			os.system("mpg321 -q internet_on_backup.mp3")
			pass

		connected = 1
		ledSwitch = 0
		time.sleep(2)

	except:
		powerSwitch = 1
		with open("error_log.csv", "a") as error_log:
			error_log.write("\n{0},Error,No internet connection.".format(strftime("%Y-%m-%d %H:%M:%S")))
		
		ledSwitch = 1
		
		Thread(target = led_red_alert).start()
		
		try:
			powerSwitch = 1
			tts = gTTS(text="Alert! All communications are down. Alert! Systems running in emergency mode. Alert! Restoring communications, priority alpha." , lang='en')
			tts.save("internet_off.mp3")
			os.system("mpg321 -q internet_off.mp3")
			os.system("mpg321 -q vader_breathe.mp3")
			os.system("mpg321 -q vader_dont_fail.mp3")
		except:
			powerSwitch = 1
			os.system("mpg321 -q internet_off_backup.mp3")
			os.system("mpg321 -q vader_breathe.mp3")
			os.system("mpg321 -q vader_dont_fail.mp3")
			pass
		
		connected = 0
		ledSwitch = 0
		time.sleep(2)
		pass

def internet_on_thread():
	global powerSwitch
	global ledSwitch
	global connected

	while True:
		time.sleep(180)

		with open("error_log.csv", "a") as error_log:
			error_log.write("\n{0},Log,Testing Internet connection.".format(strftime("%Y-%m-%d %H:%M:%S")))

		if connected == 1:
			try:
				powerSwitch = 0
				urllib.request.urlopen('http://216.58.207.206')
				#urllib.urlopen('http://216.58.207.206', timeout=4)

				with open("error_log.csv", "a") as error_log:
					error_log.write("\n{0},Log,We have an internet connection.".format(strftime("%Y-%m-%d %H:%M:%S")))
				
				connected = 1

			except:
				powerSwitch = 1
				with open("error_log.csv", "a") as error_log:
					error_log.write("\n{0},Error,No internet connection.".format(strftime("%Y-%m-%d %H:%M:%S")))
				
				ledSwitch = 1
				
				Thread(target = led_red_alert).start()
				
				try:
					powerSwitch = 1
					tts = gTTS(text="Alert! All communications are down. Alert! Systems running in emergency mode. Alert! Restoring communications, priority alpha." , lang='en')
					tts.save("internet_off.mp3")
					os.system("mpg321 -q internet_off.mp3")
					os.system("mpg321 -q vader_breathe.mp3")
					os.system("mpg321 -q vader_dont_fail.mp3")
				except:
					powerSwitch = 1
					os.system("mpg321 -q internet_off_backup.mp3")
					os.system("mpg321 -q vader_breathe.mp3")
					os.system("mpg321 -q vader_dont_fail.mp3")
					pass
				
				ledSwitch = 0
				connected = 0
				time.sleep(2)
				pass

		elif connected == 0:
			try:
				powerSwitch = 0
				urllib.request.urlopen('http://216.58.192.142')

				with open("error_log.csv", "a") as error_log:
					error_log.write("\n{0},Log,We have an internet connection.".format(strftime("%Y-%m-%d %H:%M:%S")))
				
				ledSwitch = 1
				
				Thread(target = led_green_alert).start()
				
				try:
					powerSwitch = 0
					tts = gTTS(text="Code green! All communication systems are online and working within normal parameters." , lang='en')
					tts.save("internet_on.mp3")
					os.system("mpg321 -q internet_on.mp3")
				except:
					powerSwitch = 1
					os.system("mpg321 -q internet_on_backup.mp3")
					pass

				ledSwitch = 0
				connected = 1
				time.sleep(2)

			except:
				powerSwitch = 1
				with open("error_log.csv", "a") as error_log:
					error_log.write("\n{0},Error,No internet connection.".format(strftime("%Y-%m-%d %H:%M:%S")))
				
				connected = 0
				pass
