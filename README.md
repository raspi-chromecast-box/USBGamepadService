# USB Gamepad Service

## 1.) Crontab Stuff

		0 16   *   *   *    /sbin/shutdown -r
		31 22 * * * /usr/local/bin/restartMotionServerWithDelay
		01 10 * * * systemctl stop motion-script.service
		@reboot /usr/local/bin/restartMotionServerWithDelay

## 2.) USB Gamepad Watcher Service
### [usb-gamepad-watcher.service](https://github.com/raspi-chromecast-box/USBGamepadService/blob/master/usb-gamepad-watcher.service)
I don't know if there is a better way to do this, but this is a Systemd .service file that launches a shell script , which then launches a python script and attempts to restart if failure.


## 3.) Shell Script to Launch JoyStickInput.py
### [start-python-script.sh](https://github.com/raspi-chromecast-box/USBGamepadService/blob/master/start-python-script.sh)

## 4.) Shell Script to Launch JoyStickInput.py With Delay
### [start-python-script-with-delay.sh](https://github.com/raspi-chromecast-box/USBGamepadService/blob/master/start-python-script-with-delay.sh)
Useful for launching on reboot, because even if you use things like "After=network.target" , things usually are not ready.
So if you just wait like 2 minutes , then its normally "safe" to actually start the python script.

## 5.) Python Script that Polls /dev/input/event${#}
### [JoyStickInput.py](https://github.com/raspi-chromecast-box/USBGamepadService/blob/master/JoyStickInput.py)