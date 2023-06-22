import tensorflow as tf
import cv2
import numpy as np

class Detector:
    def __init__(self):
        self.interpreter = tf.lite.Interpreter(model_path='model/model.tflite')
        self.interpreter.allocate_tensors()
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

        self.input_shape = self.input_details[0]['shape']

    def detect(self, cv_image):
        # Transform OpenCV image into a tensor.
        resized_image_to_input_shape = cv2.resize(cv_image, (self.input_shape[1], self.input_shape[2]))
        input_data = np.array(resized_image_to_input_shape[np.newaxis, ...], dtype=np.uint8)
        self.interpreter.set_tensor(self.input_details[0]['index'], input_data)

        # Generate prediction.
        self.interpreter.invoke()

        # Get all the information about the prediction result.
        boxes = self.interpreter.get_tensor(self.output_details[0]['index'])
        classes = self.interpreter.get_tensor(self.output_details[1]['index'])
        scores = self.interpreter.get_tensor(self.output_details[2]['index'])
        num = self.interpreter.get_tensor(self.output_details[3]['index'])


        #image_cv = cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB)

        # Get initial image size.
        height, width, _ = cv_image.shape

        # Look at each detected object.
        for i in range(int(num[0])):
            # If the object was detected with the highest confidence.
            if scores[0][i] == max(scores[0]):
                # Get bounding box coordinates.
                ymin, xmin, ymax, xmax = boxes[0][i]

                # Transform bounding box coordinates into absolute.
                xmin = int(xmin * width)
                xmax = int(xmax * width)
                ymin = int(ymin * height)
                ymax = int(ymax * height)

                return (True, (xmin, ymin, xmax-xmin, ymax-ymin))

#det = Detector()
#image_cv = cv2.imread('/Users/rodion/Desktop/yolo/yolov5/shahed_dataset_1/test/ahrsjicitmncgieigufifzyp0000.png')
#ret, bbox = det.detect(image_cv)
#cv2.rectangle(image_cv, (bbox[0], bbox[1]), (bbox[0]+bbox[2], bbox[1]+bbox[3]), (0, 255, 0), 2)
#cv2.imwrite('result.jpg', image_cv)
