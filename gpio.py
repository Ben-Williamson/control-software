from rpi_rf import RFDevice
from time import sleep

rfdevice = RFDevice(17)
rfdevice.enable_tx()

On_Codes = [4216115, 4216259, 4216579, 4218115, 4224259]
Off_Codes = [4216124, 4216268, 4216588, 4218124, 4224268]

Numbers = ["one", "two", "three", "four", "five"]

def plugOn(num):
	rfSend(On_Codes[Numbers.index(num)])

def plugOff(num):
	rfSend(Off_Codes[Numbers.index(num)])

def rfSend(code):
	for i in range(0, 4):
		rfdevice.tx_code(code, 1, 181)
