from Servo import Servo
import time
from Sensor import *


class Robot(object):
    def __init__(self, my_servo):
        super().__init__()
        self._servo = my_servo

    def begin(self):
        while True:
            if search():  # 如果货物在范围内，执行：
                time.sleep(1000)
                self._servo.angle = 90  # 放下货钩，进行对接
                if test_success():  # 检测是否对接成功
                    return True  # 如果成功，执行运输任务
                else:
                    time.sleep(500)
                    self._servo.angle = 0
                    continue  # 如果未成功，则继续执行搜索任务
            else:
                search_object()  # 货物不再范围内，则执行搜寻，调整位姿

    def transport(self):
        '''
            该部分为实际运输模块
            由SDP-mini的导航系统完成
            检测到达终点后执行：返回卸货指令
        '''
        pass

    def end(self):
        while True:
            self._servo.angle = 0
            if not test_success():
                return True
            else:
                self._servo.angle = 90
                continue

    def back(self):
        '''
            该部分为实际运输模块
            由SDP-mini的导航系统完成
            检测到达起点后执行：返回初始化指令
        '''
