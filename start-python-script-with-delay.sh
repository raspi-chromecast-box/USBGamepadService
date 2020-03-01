#!/bin/bash

#sleep 2m
/bin/bash -l -c 'su morphs -c "/home/morphs/.nvm/versions/node/v12.16.1/bin/pm2 restart all"'
sleep 10
sudo systemctl restart usb-gamepad-watcher