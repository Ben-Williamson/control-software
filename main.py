import requests
from flask_cors import CORS
from flask import Flask, redirect
import time
import gpio
app = Flask(__name__)
CORS(app)

#from pushbullet import Pushbullet
#pb = Pushbullet("o.vzZ5B0KA4txWfBMP2SvmQSKVghgFdrVs")
#my_channel = pb.channels[0]

devices = ["plugone", "plugtwo", "plugthree", "plugfour", "plugfive"]
states = ["off", "off", "off", "off", "off"]

def notif(device, state):
    requests.get("http://localhost:5000/" + device + "/" + state)

def logs(content):
    #push = my_channel.push_note("Alexa", content.lower().title())
    return

def recordState(device, state):
    del states[devices.index(device)]
    states.insert(devices.index(device), state)

@app.route('/<device>')
def getState(device):
    return states[devices.index(device)]

@app.route('/plug<num>/<state>')
def test(num, state):
	if(state == "on"):
		gpio.plugOn(num)
		notif("plug" + num, state)
		recordState("plug" + num, "on")
	else:
		gpio.plugOff(num)
		notif("plug" + num, state)
		recordState("plug" + num, "off")
	return "done"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
