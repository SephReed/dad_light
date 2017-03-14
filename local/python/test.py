#! /usr/bin/python
#
import subprocess
import random
from flup.server.fcgi import WSGIServer 
import sys, urlparse





def setPWM(gpio_num, value) :
	value *= value
	print value
	e = 'echo "'+str(gpio_num)+'='+str(value)+'" > /dev/pi-blaster'
	subprocess.call(e, shell=True)


def app(environ, start_response):
	start_response("200 OK", [("Content-Type", "text/html")])
	  
	i = urlparse.parse_qs(environ["QUERY_STRING"])
	yield ('&nbsp;')

	if "q" in i:
		yield (i['q'][0])

	setPWM(18, random.uniform(0.0, 1.0))






WSGIServer(app).run()
