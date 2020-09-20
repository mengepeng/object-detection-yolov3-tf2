#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@ScriptName  : detection_main.py
@Project     : Object-Detection-YOLOv3-TF2
@Author      : Meng Peng
@Date        : 10-09-2020
@Description :
"""
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'
from yolov3.yolov3 import create_yolo
from yolov3.utils import load_yolo_weights, detect_image, detect_video, detect_realtime
from yolov3.configs import *

image_path = "./data/city.jpg"
video_path = "./data/test.mp4"

if YOLO_FRAMEWORK == "tf":
    if YOLO_TYPE == "yolov3":
        Darknet_weights = YOLO_V3_TINY_WEIGHTS if YOLO_TINY else YOLO_V3_WEIGHTS
        yolo = create_yolo(input_size=YOLO_INPUT_SIZE, classes=YOLO_COCO_CLASSES)
        load_yolo_weights(yolo, Darknet_weights)
    else:
        pass
else:
    pass

# test
detect_image(yolo, image_path, "./data/city_pred.jpg", input_size=YOLO_INPUT_SIZE, show=True, rectangle_colors=(255, 0, 0))
# detect_video(yolo, video_path, "./data/test_pred.mp4", input_size=YOLO_INPUT_SIZE, show=True, rectangle_colors=(255, 0, 0))
# detect_realtime(yolo, '', input_size=YOLO_INPUT_SIZE, show=True, rectangle_colors=(255, 0, 0))

