#!/bin/bash
function is_int() { return $(test "$@" -eq "$@" > /dev/null 2>&1); }
ssh-add -D
git config --global --unset user.name
git config --global --unset user.email
git config user.name "raspi-chromecast-box"
git config user.email "raspiccbox03@gmail.com"
ssh-add -k /Users/morpheous/.ssh/githubraspiccbox3

git remote add origin git@github.com:raspi-chromecast-box/USBGamepadService.git
git pull origin master