from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time

#create flask app server
app = Flask(__name__)

#define pins
in1 = 24
in2 = 23
ENA = 25
temp1 = 1
servoPIN = 17

#setting up pins to receive information 
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(ENA,GPIO.OUT)
#initial setting low
GPIO.output(in2,GPIO.LOW)
GPIO.output(in1,GPIO.LOW)
GPIO.output(servoPIN, GPIO.LOW)
p = GPIO.PWM(ENA, 1000) #set DC PWM to 1000
q = GPIO.PWM(servoPIN, 50) #set servo PWM to 50Hz
GPIO.setwarnings(False)
#initial PWM signal
p.start(75)
q.start(7.5)

@app.route('/')
def index():
#returns the HTML file template 
    return render_template('index.html')

#linking the python functions to the flask buttons

@app.route('/<action>')
def left(action):
    if action == "on":
        q.ChangeDutyCycle(5)
        time.sleep(.5)
        #returns homepage
        return render_template('index.html')

   
@app.route('/<action>')
def forward(action):
    if action == "on":
        GPIO.output(in2, GPIO.HIGH)
        GPIO.output(in1, GPIO.LOW)
        #returns homepage
        return render_template('index.html')

@app.route("/<action>")
def backward(action):
    if action == "on":
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in1,GPIO.HIGH)
        #returns homepage
        return render_template('index.html')

@app.route("/center")
def center():
    if action == "on":
	q.ChangeDutyCycle(7.5)
	time.sleep(.5)
        #returns homepage
        return render_template('index.html')

@app.route("/right")
def right():
    if action == "on":
	q.ChangeDutyCycle(10)
	time.sleep(.5)
        #returns homepage
        return render_template('index.html')
	

@app.route('/<action>')
def stop(action):
    if action == "on":
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in1, GPIO.LOW)
        #returns homepage
        return render_template('index.html')


#takes IP address of raspberry pi for web server

if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.11')

