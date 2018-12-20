# My keras-yolo3

[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)

## Introduction

My own Keras implementation of YOLOv3 (Tensorflow backend) inspired by [qqwweee/keras-yolo3](https://github.com/qqwweee/keras-yolo3).

---
## TO-DO
List of tasks:
- [ ]: **All-tools-included** Packed tools from dataset creation to final predicts
- [ ]: **Baseline**. Evaluation framework
- [ ]: **Avoid convert**. Implement YOLO v3 in Keras directly. Hard

---
## Set-up

1. Download YOLOv3 weights from [YOLO website](http://pjreddie.com/darknet/yolo/).
`wget https://pjreddie.com/media/files/yolov3.weights`
2. Convert the Darknet YOLO model to a Keras model.
`python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5`
3. Run YOLO detection.
```
python predict.py [OPTIONS...] --image, for image detection mode,
python predict.py [video_path] [output_path (optional)] for video detection mode OR
python predict.py [--webcam] for webcam detection

```

### Usage
Use --help to see usage of yolo_video.py:
```
usage: predict.py [-h] [--model MODEL] [--anchors ANCHORS]
                     [--classes CLASSES] [--gpu_num GPU_NUM]
                     [--image] [--webcam]
                     [--input] [--output]

positional arguments:
  --input        Input path
  --output       Output path

optional arguments:
  -h, --help         show this help message and exit
  --model MODEL      path to model weight file, default model_data/yolo.h5
  --anchors ANCHORS  path to anchor definitions, default
                     model_data/yolo_anchors.txt
  --classes CLASSES  path to class definitions, default
                     model_data/coco_classes.txt
  --gpu_num GPU_NUM  Number of GPU to use, default 1
  --image            Image detection mode
  --webcam           Webcam detection mode
```

## Training

1. Generate your own annotation file and class names file.  
    One row for one image;  
    Row format: `image_file_path box1 box2 ... boxN`;  
    Box format: `x_min,y_min,x_max,y_max,class_id` (no space).  
    For VOC dataset, try `python voc_annotation.py`  
    An example:
    ```
    path/to/img1.jpg 50,100,150,200,0 30,50,200,120,3
    path/to/img2.jpg 120,300,250,600,2
    ...
    ```

2. Modify kmeans.py path and number of clusters. Then run it and copy the new `yolo_anchors.txt` file to the `model_data` folder.

3. Modify train.py paths and strategy and start training.  
    `python train.py`  
    Use your trained weights or checkpoint weights with command line option `--model model_file` when using predict.py
    Remember to modify class path or anchor path, with `--classes class_file` and `--anchors anchor_file`.

If you want to use original pretrained weights for YOLOv3:  
    1. `wget https://pjreddie.com/media/files/yolov3.weights`    
    2. `python convert.py yolov3.cfg yolov3.weights model_data/yolo_weights.h5`  
    4. use model_data/yolo_weights.h5 in train.py


## Research
List of resources that could be useful:
- Background images data set: http://vision.cs.princeton.edu/projects/2010/SUN/
- Number plate recognition with Tensorflow: http://matthewearl.github.io/2016/05/06/cnn-anpr/ code: https://github.com/matthewearl/deep-anpr
- Deep Logo (a brand logo recognition system using deep convolutional neural networks): https://github.com/satojkovic/DeepLogo
- Deep Learning Logo Detection with Data Expansion by Synthesising Context: https://arxiv.org/pdf/1612.09322.pdf
- Scalable Deep Learning Logo Detection: https://arxiv.org/pdf/1803.11417.pdf
- QMUL-OpenLogo: Open Logo Detection Challenge: https://qmul-openlogo.github.io/
- Open Logo Detection Challenge (2018): https://arxiv.org/pdf/1807.01964.pdf
- Open Set Logo Detection and Retrieval (2017): https://arxiv.org/pdf/1710.10891.pdf
- LOGO-Net. Large-scale Deep Logo Detection and Brand Recognition
with Deep Region-based Convolutional Networks: https://arxiv.org/pdf/1511.02462.pdf
- Deep Learning for Logo Recognition: https://arxiv.org/pdf/1701.02620.pdf


## Data sets
### Supervised Logo images
- QMUL-OpenLogo: https://drive.google.com/open?id=1p1BWofDJOKXqCtO0JPT5VyuIPOsuxOuj
- QMUL-OpenLogo (Supplyment Imageset List for OpenLogo Semi-Supervised Challenge): https://drive.google.com/file/d/1jvPAik5mGziKsq4Qsgu7GhiLSWlEwDSQ/view
- FlickrLogo-32: http://www.multimedia-computing.de/flickrlogos/
- WebLogo-2M: http://www.eecs.qmul.ac.uk/~hs308/WebLogo-2M.html/
- TopLogo-10: http://www.eecs.qmul.ac.uk/~hs308/qmul_toplogo10.html/
- Flickr Logo 27: http://image.ntua.gr/iva/datasets/flickr_logos/
- Logo32plus: http://www.ivl.disco.unimib.it/activities/logo-recognition/
- BelgaLogos: http://www-sop.inria.fr/members/Alexis.Joly/BelgaLogos/BelgaLogos.html
- Logos-In-The-Wild: https://www.iosb.fraunhofer.de/servlet/is/78045/
- SportsLogo: https://ieeexplore.ieee.org/document/8237781

### Background images
- SUN Database. Scene Categorization Benchmark: http://vision.cs.princeton.edu/projects/2010/SUN/

### Useful tools
- Google Images Downloader script: https://github.com/hardikvasa/google-images-download
- Web free image labeling tool: https://github.com/NaturalIntelligence/imglab
- Standalone free image labeling tool 1: https://github.com/tzutalin/labelImg
- Standalone free image labeling tool 2: https://github.com/wkentaro/labelme
