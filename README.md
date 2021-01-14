# Black-smoke-Trucks-Detection
A computer vision project for my undergraduate thesis. 
It's about black-smoke trucks detection.  
本科毕业论文项目，计算机视觉相关，黑烟车检测。

Source code, dataset(with labels), experiments and results, presentation slides, paper are included in this repository.  
本仓库包括了代码、数据集（带标注）、实验及结果、答辩PPT、论文。

**Keywords:** deep learning; object detection; black-smoke trucks; CNN; SSD; MXNET; gluoncv  
**关键词：** 深度学习；目标检测；黑烟车；卷积神经网络；SSD；MXNET；gluoncv


# Directory Structure 目录结构
```
├─代码 Code
│  └─ImgPreProcess
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


# 摘要 Abstract
Computer vision is one of the hottest directions of deep learning. 
Thanks to the development of data and hardware, many excellent algorithms have appeared in object detection, which is one of the fields of computer vision. 
This paper attempts to use the mainstream target detection method to achieve automatic identification of black tobacco trucks, alleviate the long-term problem of time-consuming and laborious supervision of black smoke trucks by traffic control departments, which is in line with the policy direction of the country's increasing concern for environmental issues in recent years. After completing a series of tasks, such as self-built data set of black smoke truck, a large number of image augmentation operations, building a deep neural network model based on ResNet, the application of transfer learning and the optimization of network model parameters, the final model we got reached 0.9752 mAP on the test set.

计算机视觉是深度学习炙手可热的方向之一，得益于数据、硬件的发展，计算机视觉领域之目标检测出现了很多优秀的算法。
本文尝试运用主流的目标检测方法实现对黑烟车的自动识别，减轻交管部门长期以来对黑烟车监管费时费力的问题，符合国家近年来对环境问题日益关注的政策方向。
通过完成自建黑烟车数据集，大量的图像增广操作，搭建以ResNet为骨架的深度神经网络模型，迁移学习的应用以及网络模型参数调优等一系列工作后，我们得到的最终模型在测试集上达到了0.9752的mAP。


# 数据集 Dataset

## 数据收集
图片数据集主要来源为各大搜索引擎的关键字搜索结果。
通过国内外搜索引擎搜索相关图片，对搜索结果进行爬取，一共爬取了来自国内搜索引擎的黑烟车图片234张，来自国外搜索引擎的黑烟车图片287张，原始图片共计521张。

## 图像增广预处理

## Pascal VOC数据集