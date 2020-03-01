 #!/bin/bash

# If you Need Time Window Stuff
# currenttime=$(date +%H:%M)
# if [[ "$currenttime" > "22:30" ]] || [[ "$currenttime" < "10:00" ]]; then
# 	sudo pkill -9 python
# 	set -x
# 	set -e
# 	python3 /home/pi/WORKSPACE/RaspiMotionAlarmRewrite/py_scripts/JoyStickInput.py
# else
# 	echo "Not Inside Time Window"
# fi

# Don't ask me , but I am pretty sure this equality check is required to get python to "fork" off
if [[ 1 > 0 ]]; then
	sudo pkill -9 python
	set -x
	set -e
	python3 /home/pi/WORKSPACE/RaspiMotionAlarmRewrite/py_scripts/JoyStickInput.py
else
	echo "1 Not Greater Than Zero ... monkaS"
fi