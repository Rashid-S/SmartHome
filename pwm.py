#!/usr/bin/env python
# -*- coding: utf-8 -*-


import wiringpi

# GPIO pin 12 = BCM pin 18 = wiringpi pin 1
led_pin  = 1

wiringpi.wiringPiSetup()
wiringpi.pinMode(led_pin, 2)
wiringpi.pwmWrite(led_pin, 0)

def led(led_value):
    wiringpi.pwmWrite(led_pin, led_value)

# значение должно быть от 0 до 1024
led(1020)