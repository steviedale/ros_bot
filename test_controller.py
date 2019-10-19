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

	def forward(self):
		GPIO.output(right_wheel_forward, 1)
		GPIO.output(left_wheel_forward, 1)
		GPIO.output(right_wheel_backward, 0)
		GPIO.output(left_wheel_backward, 0)

	def backward(self):
		GPIO.output(right_wheel_forward, 0)
		GPIO.output(left_wheel_forward, 0)
		GPIO.output(right_wheel_backward, 1)
		GPIO.output(left_wheel_backward, 1)

	def forward_turn_right(self):
		GPIO.output(right_wheel_forward, 1)
		GPIO.output(left_wheel_forward, 0)
		GPIO.output(right_wheel_backward, 0)
		GPIO.output(left_wheel_backward, 0)

	def forward_turn_left(self):
		GPIO.output(right_wheel_forward, 0)
		GPIO.output(left_wheel_forward, 1)
		GPIO.output(right_wheel_backward, 0)
		GPIO.output(left_wheel_backward, 0)

	def backward_turn_left(self):
		GPIO.output(right_wheel_forward, 0)
		GPIO.output(left_wheel_forward, 0)
		GPIO.output(right_wheel_backward, 1)
		GPIO.output(left_wheel_backward, 0)

	def backward_turn_right(self):
		GPIO.output(right_wheel_forward, 0)
		GPIO.output(left_wheel_forward, 0)
		GPIO.output(right_wheel_backward, 0)
		GPIO.output(left_wheel_backward, 1)

	def stop(self):
		GPIO.output(right_wheel_forward, 0)
		GPIO.output(left_wheel_forward, 0)
		GPIO.output(right_wheel_backward, 0)
		GPIO.output(left_wheel_backward, 0)

	def __del__(self):
		GPIO.cleanup()

if __name__ == '__main__':
	wheel_controller = WheelController()
	command = ''
	while command != 'q':
		command = input('Enter command: ')
		if command == 'f':
			wheel_controller.forward()
		elif command == 'b':
			wheel_controller.backward()
		elif command == 'r':
			wheel_controller.forward_turn_right()
		elif command == 'l':
			wheel_controller.forward_turn_left()
		elif command == 's':
			wheel_controller.stop()

	




