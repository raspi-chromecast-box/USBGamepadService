import sys
import os
import time
import subprocess
import requests
from evdev import InputDevice, categorize, ecodes, KeyEvent
def express_publish( options ):
	try:
		print( "\nSending POST to Express Server" )
		print( options )
		response = requests.post( 'http://127.0.0.1:9696/button' , data=options )
		print( response.text )
	except Exception as e:
		print( e )
KeyCodeType = {
	'BTN_BASE4': 1 ,
	'BTN_BASE5': 2 ,
	'BTN_BASE6': 3 ,
	'BTN_BASE2': 4 ,
	'BTN_BASE3': 5 ,
	'BTN_JOYSTICK': 6 ,
	'BTN_THUMB': 7 ,
	'BTN_PINKIE': 8 ,
	'BTN_BASE': 9 ,
	'BTN_THUMB2' : 0 ,
	'BTN_TOP' : 1 ,
	'BTN_TOP2' : 2
}
TOTAL_INPUT_DEVICES = 31
def try_to_get_gamepad():
	for i in range( TOTAL_INPUT_DEVICES ):
		try:
			gamepad = InputDevice( f"/dev/input/event{i}" )
			try:
				string = str( gamepad.name )
			except Exception:
					pass
			if "DragonRise Inc." in string:
				print( f"Found DragonRise USB Gamepad on /dev/input/event{i}" )
				return gamepad
		except Exception as e:
			print( f"Couldn't Connect to /dev/input/event{i}" )
			return False
	return False

def run_read_loop():
	gamepad = try_to_get_gamepad()
	if gamepad is False:
		return False
	LAST_PRESSED_TIME = int( time.time() )
	LAST_PRESSED_COOLDOWN = 2
	try:
		for event in gamepad.read_loop():
			if event.type == ecodes.EV_KEY:
				keyevent = categorize( event )
				if keyevent.keystate == KeyEvent.key_up:
					now = int( time.time() )
					elapsed_seconds = now - LAST_PRESSED_TIME
					if elapsed_seconds < LAST_PRESSED_COOLDOWN:
						print( "\nInside Button Press Cooldown" )
						print( str( now ) + " - " + str( LAST_PRESSED_TIME ) + " === " + str( elapsed_seconds ) )
						print( str( elapsed_seconds ) + " < " + str( LAST_PRESSED_COOLDOWN ) )
						continue
					LAST_PRESSED_TIME = now
					express_publish({ "button_code": keyevent.keycode , "button_number": KeyCodeType[ keyevent.keycode ] })
	except Exception as e:
		# print( "Couldn't Read Event Loop" )
		# print( "Rebooting" )
		#os.system( "reboot -f" )
		return False


attempt_1 = run_read_loop()
print( "Couldn't Read Event Loop, Sleeping for 3 Seconds" )
time.sleep( 5 )
attempt_2 = run_read_loop()
print( "Couldn't Read Event Loop, Sleeping for 3 Seconds" )
time.sleep( 5 )
attempt_3 = run_read_loop()
print( "Couldn't Read Event Loop, Sleeping for 3 Seconds" )
time.sleep( 5 )
attempt_4 = run_read_loop()
print( "Couldn't Read Event Loop, Sleeping for 3 Seconds" )
time.sleep( 5 )
attempt_5 = run_read_loop()
print( "Couldn't Read Event Loop 5 Times in a Row" )
print( "Rebooting" )
os.system( "reboot -f" )