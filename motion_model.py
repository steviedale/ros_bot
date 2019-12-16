#!/usr/bin/env python
import time
import wheel_controller as wc

# distance from center of left wheel to center of right wheel (in cm)
l = 12.3
wheel_diameter = 6.6

wheel_controller = wc.WheelController()

rate = 0.50
delta_t = 0.50

# FORWARD
wheel_controller.set_left_wheel_angular_velocity(rate)
wheel_controller.set_right_wheel_angular_velocity(rate)
time.sleep(delta_t)

# STOP
wheel_controller.stop()
time.sleep(delta_t)

input('PRESS ENTER TO CONTINUE')

# TURN RIGHT
wheel_controller.set_left_wheel_angular_velocity(rate)
wheel_controller.set_right_wheel_angular_velocity(-rate)
time.sleep(delta_t)

# STOP
wheel_controller.stop()
time.sleep(delta_t)

input('PRESS ENTER TO CONTINUE')

# TURN LEFT
wheel_controller.set_left_wheel_angular_velocity(-rate)
wheel_controller.set_right_wheel_angular_velocity(rate)
time.sleep(delta_t)

# STOP
wheel_controller.stop()
time.sleep(delta_t)

input('PRESS ENTER TO CONTINUE')

# BACKWARDS
wheel_controller.set_left_wheel_angular_velocity(-rate)
wheel_controller.set_right_wheel_angular_velocity(-rate)
time.sleep(delta_t)

# STOP
wheel_controller.stop()
print('done')
