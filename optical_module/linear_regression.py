import numpy as np

class LinearRegression:
    def __init__(self):
        self.reset()

    def add_point(self, bbox, frame_width):
        self.route_line_points['x'].append(int(bbox[0] + bbox[2]/2))
        self.route_line_points['y'].append(int(bbox[1] + bbox[3]/2))
        self.linearity_counter += 1
        if self.linearity_counter == self.POINTS_AMOUNT:
            coeffs = np.polyfit(np.array(self.route_line_points['x']), np.array(self.route_line_points['y']), 1)
            self.line['pt1'] = (0, int(coeffs[1]))
            self.line['pt2'] = (frame_width-1, int(coeffs[0]*(frame_width-1) + coeffs[1]))
            self.status = True

    def ready_to_approx(self):
        return self.status

    def points(self):
        if not self.status:
            return None
        return (self.line['pt1'], self.line['pt2'])

    def reset(self):
        self.POINTS_AMOUNT = 5
        self.route_line_points = {'x': [], 'y': []}
        self.linearity_counter = 0
        self.line = {'pt1': (), 'pt2': ()}
        self.status = False
