#! /usr/bin/python
#
import subprocess
import random
from flup.server.fcgi import WSGIServer 
import sys, urlparse
import math
from time import sleep





def setPWM(gpio_num, value) :
	value *= value
	print value
	e = 'echo "'+str(gpio_num)+'='+str(value)+'" > /dev/pi-blaster'
	subprocess.call(e, shell=True)


def app(environ, start_response):
	start_response("200 OK", [("Content-Type", "text/html")])
	  
	i = urlparse.parse_qs(environ["QUERY_STRING"])
	yield ('&nbsp;')
	# yield ('&nbsp;' + "lalal" + str(environ["QUERY_STRING"]))


	if "bright" in i:
		brightness = float(i['bright'][0])
		setPWM(18, brightness)

	elif "mode" in i:
		mode = str(i['mode'][0])
		yield(mode)
		if mode == "off":
			setPWM(18, 0)

		elif mode == "on":
			setPWM(18, 1)

		elif mode == "sawUp":
			for i in range(1000):
				setPWM(18, (i/20.0) % 1)
				sleep(0.01)

		elif mode == "sawDown":
			for i in range(1000):
				setPWM(18, 1 - ((i/20.0) % 1))
				sleep(0.01)

		elif mode == "wave":
			for i in range(1000):
				value = (math.sin(i/20.0)/2) + 0.5
				setPWM(18, value)
				sleep(0.01)
	






WSGIServer(app).run()
