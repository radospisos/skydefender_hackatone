from controller_module.motors import Motors

class Controller():
    def __init__(self):
        self.x_Moto = Motors(stepPin=32,dirPin=22)
        self.y_Moto = Motors(stepPin=33,dirPin=24)
        self.pan_current = self.x_Moto.get_XCurrentAngle() # X - горизрнт
        self.tilt_current = self.y_Moto.get_YCurrentAngle()

    def full_range_scan(self):
        '''
        This method should use motors to rotate camera on the full range of scanning.
        In case of the mini-model this range is 180 degrees.
        '''
        while True:
            if self.pan_current !=0 and self.pan_current <=180:
                self.x_Moto.move(self.pan_current, 0)
                self.pan_current -= 1
            elif self.pan_current <=90 and self.pan_current !=180:
                self.x_Moto.move(self.pan_current, 1)
                self.pan_current += 1
    def sector_scan(self, lhs_angle, rhs_angle):
        '''
        This method should perform scanning in a defined sector from lhs_angle to rhs_angle.
        In case of the mini-model these angles cannot be less than 0 degress or more than 180 degrees.
        '''
        self.pan_current = (lhs_angle + rhs_angle) / 2
        self.x_Moto.move(self.pan_current)
        while True:
            for self.pan_current in range(lhs_angle, rhs_angle, 1):
                self.x_Moto.move(self.pan_current)
            for self.pan_current in range(rhs_angle, lhs_angle, -1)
                self.x_Moto.move(self.pan_current)
        pass

    def sector_fix(self, angle):
        '''
        This method should move camera on a defined angle and fix it in that position.
        '''
        pass

    def follow(self, bbox):
        '''
        This method should move camera to the position in which the given bounding box would be in the center of a frame.
        '''
        pass
