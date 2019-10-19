#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

right_wheel_forward = 7
right_wheel_backward = 8
left_wheel_forward = 9
left_wheel_backward = 10

class WheelController:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        GPIO.setup(right_wheel_forward, GPIO.OUT)
        GPIO.setup(right_wheel_backward, GPIO.OUT)
        GPIO.setup(left_wheel_backward, GPIO.OUT)
        GPIO.setup(left_wheel_forward, GPIO.OUT)

        self.right_forward_pwm = GPIO.PWM(right_wheel_forward, 100)
        self.right_backward_pwm = GPIO.PWM(right_wheel_backward, 100)
        self.left_forward_pwm = GPIO.PWM(left_wheel_forward, 100)
        self.left_backward_pwm = GPIO.PWM(left_wheel_backward, 100)

    def __del__(self):
        GPIO.cleanup()


    def set_right_wheel_angular_velocity(self, angular_velocity):
        if angular_velocity > 0:
            self.right_forward_pwm.start(abs(int(angular_velocity*100)))
            GPIO.output(right_wheel_forward, 1)
            GPIO.output(right_wheel_backward, 0)
        else:
            self.right_backward_pwm.start(abs(int(angular_velocity*100)))
            GPIO.output(right_wheel_backward, 1)
            GPIO.output(right_wheel_forward, 0)

    def set_left_wheel_angular_velocity(self, angular_velocity):
        if angular_velocity > 0:
            self.left_forward_pwm.start(abs(int(angular_velocity*100)))
            GPIO.output(left_wheel_forward, 1)
            GPIO.output(left_wheel_backward, 0)
        else:
            self.left_backward_pwm.start(abs(int(angular_velocity*100)))
            GPIO.output(left_wheel_backward, 1)
            GPIO.output(left_wheel_forward, 0)

    def stop(self):
        GPIO.output(right_wheel_forward, 0)        
        GPIO.output(right_wheel_backward, 0)
        GPIO.output(left_wheel_forward, 0)        
        GPIO.output(left_wheel_backward, 0)               
