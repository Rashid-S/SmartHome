#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
#import ConfigParser
 
#config = ConfigParser.RawConfigParser()            #������������� ��������
#config.read("/home/pi/global_config.conf")         #������� ������
#pin_number = config.getint("relay_pins", "relay1") #���� �� ������� �������� ���������� pin_number
pin_number = 17

print "use pin:"+str(pin_number)
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)            
GPIO.setup(pin_number, GPIO.OUT)   #������������� ��� �� �������� ������
GPIO.output(pin_number, GPIO.LOW)  #������ ���������� ���� �� ������