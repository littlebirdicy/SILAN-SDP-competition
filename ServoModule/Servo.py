class Servo(object):
    '''
        usage:
            Servo(pin, angle)
            angle is the initial position
    '''

    def __init__(self, pin, angle):
        self._pin = pin
        self._angle = angle

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, new_angle):
        if new_angle > 180 or new_angle < 0:
            raise ValueError("angle must be set between 0 and 180!")
        else:
            self._angle = new_angle
