from Robot import Robot
from Servo import Servo
import time
from Sensor import *


# 主程序
my_servo = Servo(9, 0)
my_robot = Robot(my_servo)
while True:
    my_robot.begin()
    my_robot.transport()
    my_robot.end()
    my_robot.back()
