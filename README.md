# Black-smoke-Trucks-Detection

A computer vision project for my undergraduate thesis. 
It's about black-smoke trucks detection.  
本科毕业论文项目，计算机视觉相关，黑烟车检测。

Source code, datasets(with labels), experiments and results, presentation slides, paper are included in this repository.  
本仓库包括了代码、数据集（带标注）、实验及结果、答辩PPT、论文。


# Directory Structure 目录结构

```
├─代码 Code
│  └─ImgPreProcess
│      └─__pycache__
├─实验 Experiment
│  ├─图像增广 Image augmentation
│  ├─微调实验 Fine-tune
│  ├─最佳学习率 Best learning rate
│  ├─最佳批大小 Best batch size
│  └─网络选择实验 Network model selection
├─实验结果 Result
│  ├─检测效果国内 Result first-class image (China)
│  ├─检测效果国外 Result second-class image (Foreign)
│  └─误识别 Error Case
├─数据集 Dataset
│  └─VOCtemplate
│      └─VOC2019
│          ├─Annotations
│          ├─ImageSets
│          │  └─Main
│          ├─JPEGImages
│          └─third
├─答辩 Presentation
└─论文 Paper
    ├─图片 Image
    ├─杂项 Misc
    └─草稿 Script
```