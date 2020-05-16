from Robot import Robot
from Servo import Servo
import time
from Sensor import *


# 主程序
my_servo = Servo(9, 0)  # 将舵机初始化为引脚9，初始角度0°
my_robot = Robot(my_servo)  # 用舵机实例初始化robot
while True:
    my_robot.begin()  # 装货阶段，连接货箱
    my_robot.transport()  # 运输阶段
    my_robot.end()  # 卸货阶段，断开连接
    my_robot.back()  # 返回出发点，继续运输
