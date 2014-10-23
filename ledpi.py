#!/usr/bin/env python
# first line points to path for python

#import the web.py library
import web

import RPi.GPIO as GPIO

#dont bug me with warnings
GPIO.setwarnings(False)

# to use Raspberry Pi bcm numbers
GPIO.setmode(GPIO.BCM)

# set up GPIO output channels
GPIO.setup(28, GPIO.OUT)  # Green
GPIO.setup(29, GPIO.OUT)  # Red
GPIO.setup(30, GPIO.OUT)  # Blue

#make a status global variable
global status
#fill it with zeroes
status = [0, 0, 0]

#templates are in templates folder
render = web.template.render('templates/')

urls = ('/', 'index')
app = web.application(urls, globals())

G = GPIO.PWM(28, 1000)
G.start(100)


class index:

    def __init__(self):
        self.hello = "Pumpkin Pi!"

    def GET(self):
        getInput = web.input(turn="")
        command = str(getInput.turn)
    #control commands
        if command == "1":
            if status[0] == 0:
                #toggle Green
                status[0] = 1
                G.ChangeDutyCycle(0)
                #GPIO.output(28, GPIO.LOW)
                print 'Green ON'
                return render.index(status)
            elif status[0] == 1:
                status[0] = 0
                G.ChangeDutyCycle(100)
                #GPIO.output(28, GPIO.HIGH)
                print 'Green OFF'
                return render.index(status)
            else:
                print 'error'
            return render.index(status)

        if command == "2":
            if status[1] == 0:
                #toggle Red
                status[1] = 1
                GPIO.output(29, GPIO.LOW)
                print 'Red ON'
                return render.index(status)
            elif status[1] == 1:
                status[1] = 0
                GPIO.output(29, GPIO.HIGH)
                print 'Red OFF'
                return render.index(status)
            else:
                print 'error'
            return render.index(status)

        if command == "3":
            if status[2] == 0:
                #toggle Blue
                status[2] = 1
                GPIO.output(30, GPIO.LOW)
                print 'Blue ON'
                return render.index(status)
            elif status[2] == 1:
                status[2] = 0
                GPIO.output(30, GPIO.HIGH)
                print 'Blue OFF'
                return render.index(status)
            else:
                print 'error'
            return render.index(status)

            #default
        else:
            #has to start by visiting /?turn=on
            return render.index(status)

if __name__ == "__main__":
        app.run()
