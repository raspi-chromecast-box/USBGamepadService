FROM alpine:latest
RUN apk add linux-headers
RUN apk add gcc
RUN apk add nano
RUN apk add python3-dev
RUN apk add musl-dev
RUN apk add bash
RUN apk add openrc
RUN apk add python3
RUN apk add py3-pip
RUN pip3 install requests
RUN pip3 install evdev

RUN mkdir /dev/input/
COPY event_files /dev/input/

COPY JoyStickInputDocker.py /home/

#COPY alpine-init-d-python-script /etc/init.d/
#RUN chmod +x /etc/init.d/alpine-init-d-python-script
#RUN rc-update add alpine-init-d-python-script default

# ENTRYPOINT [ "/bin/bash" ]
# ENTRYPOINT [ "/etc/init.d/alpine-init-d-python-script" , "reload" ]
ENTRYPOINT [ "python3" , "/home/JoyStickInputDocker.py" ]



# cat /proc/devices
# ls -l /dev/input/event0*
# Apparently it goes up to 31
# https://www.kernel.org/doc/Documentation/input/input.txt

# On Mac OSX Create Event Files
# for i in $(seq 0 31); do sudo mknod event$i c 13 64; done
# sudo chmod 660 *

# On Linux , one step
# for i in $(seq 0 31); do sudo mknod event$i c 13 64 -m 660; done


# sudo docker build -t alpine-button-watcher .

#sudo docker run -it \
#--privileged -v /dev/input/:/dev/input/ \
#alpine-button-watcher

#sudo apt-get install docker.io -y && \
#sudo docker-compose