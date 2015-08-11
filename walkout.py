#!/usr/bin/env python

from time import sleep
import os
import RPi.GPIO as GPIO
import random
import Adafruit_CharLCD as LCD

# Initialize LCD
lcd = LCD.Adafruit_CharLCDPlate()

# Initialize GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN) # Change song
GPIO.setup(24, GPIO.IN) # Play song
GPIO.setup(25, GPIO.IN) # Won the game

# The following players requested multiple walkout songs
# Built arrays for each user
tysons_songs = ['Awwsome.mp3', 'RainingBlood.mp3', 'SameCrew.mp3', 'WeDemBoyz.mp3']
dans_songs = ['BumpAndGrind.mp3', 'IgnitionRemix.mp3', 'Bugatti.mp3']
seans_songs = ['Champion.mp3', 'RealAmerican.mp3', 'Renegade.mp3', 'AllTheWayTurntUp.mp3', 'HowToBeTheMan.mp3']

# The next 2 lists must align with each other to play that persons song of choice
batter_names = ['Aaron M', 'Alain N', 'Andrew B', 'Dan G', 'Lukas L', 'Hector C', 'Paul B', 'Paul J', 'Ryan S', 'Sean J', 'Shaun R', 'Tyson N']

song_names = ['PartyInTheUSA.mp3', 'TurnDownForWhat.mp3', 'Blood.mp3', random.choice(dans_songs), 'WantedDeadOrAlive.mp3', 'DancingQueen.mp3', 'DownWithTheSickness.mp3', 'DancingQueen.mp3', 'FreakOnALeash.mp3', random.choice(seans_songs), 'ThriftShop.mp3', random.choice(tysons_songs)]

# Keeps track of where we are in the 2 lists
list_number = 0
battername = batter_names[list_number]
songname = song_names[list_number]

# Check to make sure song_names and  batter_names are the same length
if len(song_names) != len(batter_names):
    print("song_names and batter_names are not the same length")
    exit()

lcd.clear()
lcd.message(battername + "\n" + songname[:-4])

# Plays a greeting to let you know the system is booted and ready.
# This is helpful because you are probably running this without a monitor
# or a network connection.
os.system('sudo mpg321 Walkout.mp3')

# Wait for input, then repeat
# These could definitely be placed in functions but I was in a hurry
while True:
    if (lcd.is_pressed(LCD.SELECT)):
        # Check to make sure we arent at the end of list, start at beginning if we are.
        if list_number == len(batter_names) - 1:
            list_number = 0
            battername = batter_names[list_number]
            if battername == 'Dan G':
                songname = random.choice(dans_songs)
                lcd.clear()
                lcd.message(battername + "\n" + songname[:-4])
            elif battername == 'Tyson N':
                songname = random.choice(tysons_songs)
                lcd.clear()
                lcd.message(battername + "\n" + songname[:-4])
            elif battername == 'Sean J':
                songname = random.choice(seans_songs)
                lcd.clear()
                lcd.message(battername + "\n" + songname[:-4])
            else:
                songname = song_names[list_number]
                lcd.clear()
                lcd.message(battername + "\n" + songname[:-4])
        else:
            list_number = list_number + 1
            battername = batter_names[list_number]
            if battername == 'Dan G':
                songname = random.choice(dans_songs)
                lcd.clear()
                lcd.message(battername + "\n" + songname[:-4])
            elif battername == 'Tyson N':
                songname = random.choice(tysons_songs)
                lcd.clear()
                lcd.message(battername + "\n" + songname[:-4])
            elif battername == 'Sean J':
                songname = random.choice(seans_songs)
                lcd.clear()
                lcd.message(battername + "\n" + songname[:-4])
            else:
                songname = song_names[list_number]
                lcd.clear()
                lcd.message(battername + "\n" + songname[:-4])

    # Play current song
    if (lcd.is_pressed(LCD.LEFT)):
        playsong = "sudo mpg321 " + songname
        os.system(playsong)
    # Play song if we won the game
    if (lcd.is_pressed(LCD.RIGHT)):
        lcd.clear()
        lcd.message("WE WON!!!!!!" + "\n" + "OMG! OMG! OMG!")
        os.system('sudo mpg321 WeAreTheChampions.mp3')
    sleep(0.1) 
