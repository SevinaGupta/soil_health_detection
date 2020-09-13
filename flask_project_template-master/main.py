import RPi.GPIO as GPIO
import time, random, math, threading, datetime, locale, os, sys, Adafruit_DHT, urllib, yaml, paramiko, tweepy, requests, alsaaudio
from gtts import gTTS
from gpiozero import CPUTemperature
from time import strftime
from time import sleep
from threading import Thread


locale.setlocale(locale.LC_ALL, 'en_GB.UTF-8')

### GPIO and VARIABLES for input/outpus on the Raspberry Pi ###

# Relay
relay = 17

# Hygro
hygro = 23
hygro_Power = 24

# Led Diods
blue_one_pin = 27
blue_two_pin = 22
blue_three_pin = 5
green_one_pin = 6
green_two_pin = 26
red_one_pin = 25
red_two_pin = 16
blue_on_off_pin = 18

# GPIO Set mode to BCM instead of Board
GPIO.setmode(GPIO.BCM)

# GPIO input output
GPIO.setup(blue_one_pin, GPIO.OUT)
GPIO.setup(blue_two_pin, GPIO.OUT)
GPIO.setup(blue_three_pin, GPIO.OUT)
GPIO.setup(green_one_pin, GPIO.OUT)
GPIO.setup(green_two_pin, GPIO.OUT)
GPIO.setup(red_one_pin, GPIO.OUT)
GPIO.setup(red_two_pin, GPIO.OUT)
GPIO.setup(blue_on_off_pin, GPIO.OUT)

# Led PWM - Pulse width modulation - for pulsating lights
blue_one = GPIO.PWM(blue_one_pin, 100)
blue_two = GPIO.PWM(blue_two_pin, 100)
blue_three = GPIO.PWM(blue_three_pin, 100)
green_one = GPIO.PWM(green_one_pin, 100)
green_two = GPIO.PWM(green_two_pin, 100)
red_one = GPIO.PWM(red_one_pin, 100)
red_two = GPIO.PWM(red_two_pin, 100)
blue_on_off = GPIO.PWM(blue_on_off_pin, 100)

# Sets the diod to start at 0 - which means off
blue_one.start(0)
blue_two.start(0)
blue_three.start(0)
green_one.start(0)
green_two.start(0)
red_one.start(0)
red_two.start(0)
blue_on_off.start(0)

# Hygro reader setup
GPIO.setup(hygro, GPIO.IN)
GPIO.setup(hygro_Power, GPIO.OUT)

# Relay setup
GPIO.setup(relay, GPIO.OUT)

# Variables for logging
cpu = CPUTemperature()