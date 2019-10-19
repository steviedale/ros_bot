#!/usr/bin/env python
import time
import wheel_controller as wc

# distance from center of left wheel to center of right wheel (in cm)
l = 12.3
wheel_diameter = 6.6

wheel_controller = wc.WheelController()

rate = 0.35
wheel_controller.set_left_wheel_angular_velocity(rate)
wheel_controller.set_right_wheel_angular_velocity(rate)
time.sleep(1.0)
wheel_controller.set_left_wheel_angular_velocity(0.0)
wheel_controller.set_right_wheel_angular_velocity(0.0)
print('done')


