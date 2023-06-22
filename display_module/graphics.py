import cv2

class Graphics:
    def __init__(self):
        self.window_name = "Video"
        #cv2.namedWindow(self.window_name)
        #cv2.createButton("Back",self.back,None,cv2.QT_PUSH_BUTTON,1)

    def back(self):
        pritn('button pressed')

    def draw_default_markup(self, image):
        cx, cy = int(image.shape[1] / 2), int(image.shape[0] / 2)
        tube_r = 50
        left_top = (int(cx - tube_r), int(cy - tube_r))
        right_bot = (int(cx + tube_r), int(cy + tube_r))
        left_bot = (left_top[0], right_bot[1])
        right_top = (right_bot[0], left_top[1])

        image = cv2.line(image, left_top, (left_top[0]+20, left_top[1]), (0, 0, 0), 2)
        image = cv2.line(image, left_top, (left_top[0], left_top[1]+20), (0, 0, 0), 2)

        image = cv2.line(image, left_bot, (left_bot[0]+20, left_bot[1]), (0, 0, 0), 2)
        image = cv2.line(image, left_bot, (left_bot[0], left_bot[1]-20), (0, 0, 0), 2)

        image = cv2.line(image, right_top, (right_top[0]-20, right_top[1]), (0, 0, 0), 2)
        image = cv2.line(image, right_top, (right_top[0], right_top[1]+20), (0, 0, 0), 2)

        image = cv2.line(image, right_bot, (right_bot[0]-20, right_bot[1]), (0, 0, 0), 2)
        image = cv2.line(image, right_bot, (right_bot[0], right_bot[1]-20), (0, 0, 0), 2)

        image = cv2.line(image, (cx-10, cy), (cx+10, cy), (0, 0, 0), 2)
        image = cv2.line(image, (cx, cy-10), (cx, cy+10), (0, 0, 0), 2)
        return image

    def update_scanning_info(self, image, scanning=False, scanning_mode=None, detection=False, tracking=False, approx=False):
        scanning_status_txt = 'SCAN: ' + ('ON' if scanning else 'OFF')
        image = cv2.putText(image, scanning_status_txt, (20, 20), cv2.FONT_HERSHEY_PLAIN,
                   1, (0, 0, 0), 2, cv2.LINE_AA)
        scanning_mode_status_txt = 'SCAN MODE: '
        if scanning_mode == None:
            scanning_mode_status_txt += '--'
        elif scanning_mode == '360scan':
            scanning_mode_status_txt += 'FULL RANGE'
        elif scanning_mode == 'sector_scan':
            scanning_mode_status_txt += 'SECTOR SCAN'
        elif scanning_mode == 'sector_fix':
            scanning_mode_status_txt += 'SECTOR FIX'
        image = cv2.putText(image, scanning_mode_status_txt, (20, 40), cv2.FONT_HERSHEY_PLAIN,
                   1, (0, 0, 0), 2, cv2.LINE_AA)
        detection_status_txt = 'DETECTED: ' + ('YES' if detection else 'NO')
        image = cv2.putText(image, detection_status_txt, (20, 60), cv2.FONT_HERSHEY_PLAIN,
                   1, (0, 0, 0), 2, cv2.LINE_AA)
        tracking_status_txt = 'TRACKING: ' + ('ON' if tracking else 'OFF')
        image = cv2.putText(image, tracking_status_txt, (20, 80), cv2.FONT_HERSHEY_PLAIN,
                   1, (0, 0, 0), 2, cv2.LINE_AA)
        approx_status_txt = 'APPROXIMATION LINE: ' + ('ON' if tracking else 'OFF')
        image = cv2.putText(image, approx_status_txt, (20, 100), cv2.FONT_HERSHEY_PLAIN,
                   1, (0, 0, 0), 2, cv2.LINE_AA)
        return image

    def draw_rectangle(self, image, rectangle, color):
        x, y, w, h = rectangle
        image = cv2.rectangle(image, (int(x), int(y)), (int(x+w), int(y+h)), color, 2)
        return image

    def stop_condition(self, button):
        return cv2.waitKey(25) & 0xFF == ord(button)
