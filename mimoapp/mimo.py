import cv2
import numpy as np
import threading
       
class Mimo(object):
    def __init__(self):
        self.update_thread = threading.Thread(target=self.update, args=())
        
    def create(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        #self.result = self.frame.copy() # 현재 화면 카피
        self.update_thread = threading.Thread(target=self.update, args=())
        self.update_thread.start()
        
    def __del__(self):
        self.video.release()

    def get_frame(self):
        #image = self.result
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()
            
            