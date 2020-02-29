#!/bin/bash

#sleep 2m
/bin/bash -l -c 'su pi -c "/home/pi/.nvm/versions/node/v8.9.4/bin/pm2 restart all"'
sleep 10
sudo systemctl restart usb-gamepad-watcher