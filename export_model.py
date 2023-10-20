import cv2
from ultralytics import YOLO
import time
import numpy as np

model_path = "D:\VIT Material\VIT material\Projects\FaceRecognition-Attendance\YOLOv8\\runs\detect\\train3\weights\last.pt"
model = YOLO(model_path)

results = model.export(format="onnx", opset=12)  # export the model to ONNX format
print("Model exported to ONNX format.")
