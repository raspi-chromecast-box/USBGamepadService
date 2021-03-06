import sys
import time
import subprocess
import requests
from evdev import InputDevice, categorize, ecodes, KeyEvent

def find_event_path_of_named_joystick():
	shell_command = [ "ls" , "-la" , "/dev/input/by-id/" ]
	result = subprocess.run( shell_command , capture_output=True , universal_newlines=True )
	lines = result.stdout.split( "\n" )
	for index , line in enumerate( lines ):
		#print( str( index ) + " === " + line )
		if "usb-DragonRise_Inc._Generic_USB_Joystick-event-joystick" in line:
			event_path = line.split( "->" )
			if len( event_path ) < 1:
				continue
			event_path = event_path[ 1 ].split( "../" )
			if len( event_path ) < 1:
				continue
			return event_path[ 1 ]


our_event_path = "/dev/input/" + find_event_path_of_named_joystick()
print( our_event_path )

def express_publish( options ):
	try:
		print( "\nSending POST to Express Server" )
		print( options )
		response = requests.post( 'http://127.0.0.1:9696/button' , data=options )
		print( response.text )
	except Exception as e:
		print( e )

# Maps Button Names to the Way We Installed Physical Buttons into Wooden Box
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

gamepad = InputDevice( our_event_path )
LAST_PRESSED_TIME = int( time.time() )
# Given in Seconds , miliseconds how ? , who knows
LAST_PRESSED_COOLDOWN = 2
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
