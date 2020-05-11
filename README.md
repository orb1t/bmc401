# balloon mission computer 4.01

this is a rewrite of my raspberry pi high altitude balloon software.
while previous version was a mix of c and bash scripts, this time it's written in python (as much as possible) so better data flow is possible

new features include:

- SSDV over APRS

- better monitoring and build in tests

- web based remote control for ground operation

## installation prerequisits on raspberry pi
    sudo apt-get install git
    sudo apt-get install python3-pip
    sudo apt-get install python3-setuptools
    sudo apt-get install python3-rpi.gpio
    sudo apt-get install python3-smbus
    sudo apt-get install wiringpi
    sudo apt-get install python3-picamera
    sudo apt-get install python3-pil
    pip3 install pyserial
    
### installing adafruit bmp085 support
    git clone https://github.com/adafruit/Adafruit_Python_BMP.git
    cd Adafruit_Python_BMP/
    sudo python3 setup.py install
    
