try:
	import RPi.GPIO as GPIO 
	import time

	GPIO.setmode(GPIO.BCM)

	TRIG = 23
	ECHO = 24

	GPIO.setup(TRIG, GPIO.OUT)
	GPIO.setup(ECHO, GPIO.IN)

	def get_value_distance(x):
		values = []
		for i in range(x):
			GPIO.output(TRIG, True)
			time.sleep(0.00001)
			GPIO.output(TRIG, False)
			while GPIO.input(ECHO) == 0:
				# Pulse_Start
				p_s = time.time()
			while GPIO.input(ECHO) == 1:
				# Pulse_End
				p_e = time.time()
			# Pulse_Distance
			p_d = p_e - p_s
			# Distance
			d = p_d * 17150
			print("Leitura ", i, ": ", d, " cm")
			values.append(d)
			time.sleep(0.05)

		# Container_distance
		c_d = 10

		# Medium_Sum_Distances
		sum_d = sum(values)/x
		sum_d = c_d if sum_d > c_d else sum_d

		# Distance_Real
		d_c = c_d - sum_d

		d_c = c_d if d_c == 0 else d_c
		media =  round((d_c/c_d)*100,1)

		return media
except Exception as e:
	print(e)