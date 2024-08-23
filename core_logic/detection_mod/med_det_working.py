# detection_mod/med_det_working.py

import mediapipe as mp
import cv2
import numpy as np
from .det_base2 import BaseDetector

class MedPipeDet_1(BaseDetector):
    def __init__(self, cfg=None):
        super().__init__(cfg)
        self.f_det1 = mp.solutions.face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5)
    
    def load_mod_1(self):
        # No loading required for Mediapipe models.
        pass
    
    def detect_2(self, img):
        
        prep_img1 = self._prep_img_1(img)
        
        
        results1 = self.f_det1.process(prep_img1)
        
        if results1.detections:
            # Sort detections by bounding box size (proxy for proximity)
            ordered_faces1 = sorted(
                results1.detections, 
                key=lambda d: d.location_data.relative_bounding_box.width, 
                reverse=True
            )
            # Retain only the closest face
            self._results = [ordered_faces1[0]]
        else:
            self._results = []
    
    def _prep_img_1(self, img):
        # Convert BGR image to RGB as Mediapipe expects RGB.
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    def extract_face_1(self, img):
        # Extract the bounding box of the closest detected face
        if not self._results:
            return None
        bbox1 = self._results[0].location_data.relative_bounding_box
        ih, iw, _ = img.shape
        x, y, w, h = bbox1.xmin, bbox1.ymin, bbox1.width, bbox1.height
        return img[int(y*ih):int((y+h)*ih), int(x*iw):int((x+w)*iw)]
    
  
    def detect_all_faces(self, img):
        prep_img_all = self._prep_img_1(img)
        all_faces = self.f_det1.process(prep_img_all)
        return all_faces

# Demonstration of detection pipeline
def run_det_pipeline(img_path):
    img1 = cv2.imread(img_path)
    det1 = MedPipeDet_1()
    det1.detect_1(img1)
    closest1 = det1.extract_face_1(img1)
    if closest1 is not None:
        cv2.imshow("Closest Face", closest1)
        cv2.waitKey(0)
    else:
        print("No face found.")
