import cv2

def videostream_markup_template(image, main_rect_side=100, color=(0,0,0)):
    # Find a center of frame.
    cx, cy = int(image.shape[1] / 2), int(image.shape[0] / 2)
    tube_r = main_rect_side / 2

    # Find rectangle corners.
    left_top = (int(cx - tube_r), int(cy - tube_r))
    right_bot = (int(cx + tube_r), int(cy + tube_r))
    left_bot = (left_top[0], right_bot[1])
    right_top = (right_bot[0], left_top[1])

    # Draw lines on sides.
    image = cv2.line(image, left_top, (left_top[0]+int(main_rect_side*0.2), left_top[1]), color, 2)
    image = cv2.line(image, left_top, (left_top[0], left_top[1]+int(main_rect_side*0.2)), color, 2)

    image = cv2.line(image, left_bot, (left_bot[0]+int(main_rect_side*0.2), left_bot[1]), color, 2)
    image = cv2.line(image, left_bot, (left_bot[0], left_bot[1]-int(main_rect_side*0.2)), color, 2)

    image = cv2.line(image, right_top, (right_top[0]-int(main_rect_side*0.2), right_top[1]), color, 2)
    image = cv2.line(image, right_top, (right_top[0], right_top[1]+int(main_rect_side*0.2)), color, 2)

    image = cv2.line(image, right_bot, (right_bot[0]-int(main_rect_side*0.2), right_bot[1]), color, 2)
    image = cv2.line(image, right_bot, (right_bot[0], right_bot[1]-int(main_rect_side*0.2)), color, 2)

    # Draw "+" in the center.
    image = cv2.line(image, (cx-int(main_rect_side*0.1), cy), (cx+int(main_rect_side*0.1), cy), color, 2)
    image = cv2.line(image, (cx, cy-int(main_rect_side*0.1)), (cx, cy+int(main_rect_side*0.1)), color, 2)
    return image

def draw_default_markup(image):
    image = videostream_markup_template(image, main_rect_side=100, color=(0,0,0))
    return image

def update_scanning_info(image, scanning=False, scanning_mode=None, detection=False, tracking=False, approx=False):
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
    approx_status_txt = 'APPROXIMATION LINE: ' + ('ON' if approx else 'OFF')
    image = cv2.putText(image, approx_status_txt, (20, 100), cv2.FONT_HERSHEY_PLAIN,
               1, (0, 0, 0), 2, cv2.LINE_AA)
    return image

def draw_rectangle(image, rectangle=[0,0,0,0], color=(0,0,0)):
    try:
        x, y, w, h = rectangle
        image = cv2.rectangle(image, (int(x), int(y)), (int(x+w), int(y+h)), color, 2)
        return image
    except:
        raise ValueError('Invalid arguments into cv2.rectangle')

def draw_line(image, pt1=(0,0), pt2=(1,1), color=(0,0,0)):
    try:
        image = cv2.line(image, pt1, pt2, color, 2)
        return image
    except:
        raise ValueError('Invalid arguments into cv2.line')
