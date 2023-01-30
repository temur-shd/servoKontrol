#https://youtu.be/xHDT4CwjUQE?t=395
# Import libraries(kütüphane ekleme)

import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode (GPIO'nun modunu ayarlama)
GPIO. setmode(GPIO.BOARD)
# # Set pin 11 as an output, and set servo as pin 11 as PWM
GPIO.setup(11, GPIO.OUT)
servo = GPIO.PWM(11,50) # Note 11 is pin, 50 = 50Hz pulse

#start PWM running, but with value of 0 (pulse off) (servoyu başlatma)
servo.start(0)
print ("Waiting for 2 seconds")
time.sleep(2)
#Let's move the servo!
print ("Rotating 180 degrees in 10 steps")

# Define variable duty (Değişken görevi tanımlama)
duty = 2
# Loop for duty values from 2 to 12 (0 to 180 degrees)
while duty <= 12:
    servo.ChangeDutyCycle(duty)
    time.sleep(1)
    duty = duty + 1

# Wait a couple of seconds
time.sleep(2)
# Turn back to 90 degrees
print ("Turning back to 90 degrees for 2 seconds")
servo.ChangeDutyCyele(7)
time.sleep(2)


#turn back to 0 degrees
print ("Turning back to 0 degrees")
servo.ChangeDutyCycle(2)
time.sleep(0.5)
servo.ChangeDutyCycle(0)
#Clean things up at the end
servo.stop()
GPIO. cleanup()
print("Good by")