#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@ScriptName  : configs.py
@Project     : Object-Detection-YOLOv3-TF2
@Author      : Meng Peng
@Date        : 04-09-2020
@Description : YOLOv3 configurations
"""

# YOLO options
YOLO_FRAMEWORK              = "tf"
YOLO_TYPE                   = "yolov3"
YOLO_TINY                   = False
YOLO_V3_WEIGHTS             = "./model_data/yolov3.weights"
YOLO_V3_TINY_WEIGHTS        = "./model_data/yolov3-tiny.weights"
YOLO_COCO_CLASSES           = "./model_data/coco/coco.names"
YOLO_INPUT_SIZE             = 416
YOLO_ANCHOR_PER_SCALE       = 3
YOLO_MAX_BBOX_PER_SCALE     = 100
YOLO_IOU_LOSS_THRESH        = 0.5
YOLO_STRIDES                = [8, 16, 32]
YOLO_ANCHORS                = [[[10,  13], [16,   30], [33,   23]],
                               [[30,  61], [62,   45], [59,  119]],
                               [[116, 90], [156, 198], [373, 326]]]


# YOLOv3-TINY WORKAROUND
if YOLO_TINY:
    YOLO_STRIDES            = [16, 32, 64]
    YOLO_ANCHORS            = [[[10,  14], [23,   27], [37,   58]],
                               [[81,  82], [135, 169], [344, 319]],
                               [[0,    0], [0,     0], [0,     0]]]
