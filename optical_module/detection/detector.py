import cv2
import numpy as np
import random
import torch

class Detector:
    def __init__(self):
        self.model = torch.hub.load("ultralytics/yolov5", "yolov5s")

    def detect(self, cv_image):
        results = self.model(cv_image)
        predictions = results.pred[0].cpu().numpy()
        #print(predictions)
        winner = [0, 0, 0, 0, 0.0]
        for pred in predictions:
            if pred[-1] != 4 and pred[-1] != 33:
                continue
            xmin = int(pred[0])
            ymin = int(pred[1])
            xmax = int(pred[2])
            ymax = int(pred[3])
            if pred[-2] > winner[-1]:
                winner = [xmin, ymin, xmax, ymax, pred[-2]]
            #cv2.rectangle(cv_image, (xmin, ymin), (xmax, ymax), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 2)
            #cv2.imwrite('result.jpg', cv_image)
        if winner[-1] == 0.0:
            return (False, None)
        else:
            return (True, (winner[0], winner[1], winner[2]-winner[0], winner[3]-winner[1]))

#det = Detector()
#image_cv = cv2.imread('/Users/rodion/Desktop/yolo/yolov5/shahed_dataset_1/test/ahrsjicitmncgieigufifzyp0000.png')
#image_cv = cv2.imread('/Users/rodion/Desktop/t2.jpg')
#ret, bbox = det.detect2(image_cv)
#ret, bbox = det.detect(image_cv)
#cv2.rectangle(image_cv, (bbox[0], bbox[1]), (bbox[0]+bbox[2], bbox[1]+bbox[3]), (0, 255, 0), 2)
#cv2.imwrite('result.jpg', image_cv)
