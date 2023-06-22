from controller_module.motors import Motors

class Controller():
    def __init__(self):
        self.x_Moto = Motors(stepPin=32,dirPin=22)
        self.y_Moto = Motors(stepPin=33,dirPin=24)
        pan_mid = 90 # X - горизрнт
        tilt_mid = 45 # Y - вертикаль

    def full_range_scan(self):
        '''
        This method should use motors to rotate camera on the full range of scanning.
        In case of the mini-model this range is 180 degrees.
        '''
        pass

    def sector_scan(self, lhs_angle, rhs_angle):
        '''
        This method should perform scanning in a defined sector from lhs_angle to rhs_angle.
        In case of the mini-model these angles cannot be less than 0 degress or more than 180 degrees.
        '''
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
