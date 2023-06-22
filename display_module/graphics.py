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

    def show_image(self, image):
        cv2.imshow(self.window_name, image)

    def show_work_image(self, image):
        self.show_image(self.draw_default_markup(image))

    def draw_rectangle(self, image, rectangle, color):
        image = cv2.rectangle(image, (int(x), int(y)), (int(x+w), int(y+h)), color, 2)
        return image

    def stop_condition(self, button):
        return cv2.waitKey(25) & 0xFF == ord(button)
