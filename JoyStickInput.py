import sys
import time
import subprocess
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

# ToBe Replaced By Local HTTP Request to "WebServer"
def launch_py_script_as_os_command( py_script_path ):
	shell_command = [ "python3" , py_script_path , "--uri" , "spotify:track:4qetR2UUyBeUrJ9DbYrpVQ" ]
	result = subprocess.run( shell_command , capture_output=False , universal_newlines=True )
	print( result )

gamepad = InputDevice( our_event_path )
LAST_PRESSED_TIME = int( time.time() )
# Given in Seconds , miliseconds how ? , who knows
LAST_PRESSED_COOLDOWN = 2
for event in gamepad.read_loop():
	if event.type == ecodes.EV_KEY:
		keyevent = categorize( event )
		if keyevent.keystate == KeyEvent.key_up:

			now = int( time.time() )
			duration = now - LAST_PRESSED_TIME
			if duration < LAST_PRESSED_COOLDOWN:
				print( "Inside Button Press Cooldown" )
				continue
			LAST_PRESSED_TIME = now

			if keyevent.keycode[ 0 ] == 'BTN_JOYSTICK':
				print( "6" )
				sys.stdout.flush()
			elif keyevent.keycode == 'BTN_THUMB':
				print( "7" )
				sys.stdout.flush()
			elif keyevent.keycode == 'BTN_THUMB2':
				print( "10" )
				sys.stdout.flush()
			elif keyevent.keycode == 'BTN_TOP':
				print( "11" )
				sys.stdout.flush()
			elif keyevent.keycode == 'BTN_TOP2':
				print( "12" )
				sys.stdout.flush()
			elif keyevent.keycode == 'BTN_PINKIE':
				print( "8" )
				sys.stdout.flush()
			elif keyevent.keycode == 'BTN_BASE':
				print( "9" )
				sys.stdout.flush()
			elif keyevent.keycode == 'BTN_BASE4':
				print( "1" )
				launch_py_script_as_os_command( "/home/morphs/WORKSPACE/PYTHON/RaspiChromeCastBoxPortable/COMMANDS/SPOTIFY/Test.py" )
				sys.stdout.flush()
			elif keyevent.keycode == 'BTN_BASE5':
				print( "2" )
				sys.stdout.flush()
			elif keyevent.keycode == 'BTN_BASE6':
				print( "3" )
				sys.stdout.flush()
			elif keyevent.keycode == 'BTN_BASE2':
				print( "4" )
				sys.stdout.flush()
			elif keyevent.keycode == 'BTN_BASE3':
				print( "5" )
				sys.stdout.flush()
			elif keyevent.keycode == 'BTN_BASE4':
				print( "12" )
				sys.stdout.flush()
