import subprocess

e = 'echo "18=1" > /dev/pi-blaster'
subprocess.call(e, shell=True)