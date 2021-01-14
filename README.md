# Black-smoke-Trucks-Detection
A computer vision project for my undergraduate thesis. 
It's about black-smoke trucks detection.  
本科毕业论文项目，计算机视觉相关，黑烟车检测。

Source code, dataset(with labels), experiments and results, presentation slides, paper are included in this repository.  
本仓库包括了代码、数据集（带标注）、实验及结果、答辩PPT、论文。

**Keywords:** deep learning; object detection; black-smoke trucks; CNN; SSD; MXNET; gluoncv  
**关键词：** 深度学习；目标检测；黑烟车；卷积神经网络；SSD；MXNET；gluoncv


# 目录结构 Directory Structure
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


# 研究背景 Background
<p align="center"><img src="https://raw.githubusercontent.com/f1amingo/Black-Smoke-Trucks-Detection/main/Image/background.png"></p>


# 数据集 Dataset

## 数据收集 Data Gathering
图片数据集主要来源为各大搜索引擎的关键字搜索结果。
通过国内外搜索引擎搜索相关图片，对搜索结果进行爬取，一共爬取了来自国内搜索引擎的黑烟车图片234张，来自国外搜索引擎的黑烟车图片287张，原始图片共计521张。
<p align="center"><img src="https://raw.githubusercontent.com/f1amingo/Black-Smoke-Trucks-Detection/main/Image/data-gathering.png"></p>

## 数据预处理 Preprocessing
使用离线图像增广(Image Augmentation)对原始图片进行处理，扩充数据集。
<p align="center"><img src="https://raw.githubusercontent.com/f1amingo/Black-Smoke-Trucks-Detection/main/Image/data-processing.png"></p>

## Pascal VOC数据集 Pascal VOC Dataset
我们根据Pascal VOC官方数据文件夹结构来组织数据集。黑烟车标注工具为开源软件[labelImg](https://github.com/tzutalin/labelImg) 。
<p align="center"><img src="https://raw.githubusercontent.com/f1amingo/Black-Smoke-Trucks-Detection/main/%E8%AE%BA%E6%96%87%20Paper/%E5%9B%BE%E7%89%87%20Image/labelImg.png"></p>


# 实验环境 Environment
本文实验环境为租用的带GPU的云服务器，基本配置如下：  
**硬件环境：**
- CPU：Intel(R) Xeon(R) CPU E5-2660 v3 2.60GHz（3核）
- GPU：Nvida TITAN X 显存12G
- 内存：16G

**软件环境：**
- 操作系统：Ubuntu 16.04
- CUDA版本：10.0
- cuDNN版本：7.4
- Python：3.76
- MXNet版本：mxnet-cu100 1.4.0.post0
- gluoncv版本：gluoncv 0.4.0.post0


# 实验 Experiment

## 迁移学习与微调 Transfer Learning and Fine Tune
我们使用迁移学习（transfer learning）的方法，大大缩短了训练时间，并且训练出的模型在测试集上的表现也更好。
我们选择使用在PASCAL VOC数据集上预训练得到原模型，对输出层进行修改后，在黑烟车数据集上进行微调训练。
<p align="center"><img src="https://raw.githubusercontent.com/f1amingo/Black-Smoke-Trucks-Detection/main/Image/transfer-learning.png"></p>

## 网络结构比较 Network Model Comparison
我们使用Gluoncv在PASCAL VOC数据集上预训练好的mobilenet1、resnet50、vgg16_atrous三个基础网络模型，并使用迁移学习，修改基础网络模型的输出层，然后以较小的学习率进行训练微调。  
具体的，我们使用512*512大小的图像作为网络模型的输入，优化算法为SGD，batch size设置为16，learning rate设置为0.001分别对三个预训练好的模型进行微调，训练完25个epochs后，各模型在测试集上的mAP变化如下图：
<p align="center"><img src="https://raw.githubusercontent.com/f1amingo/Black-Smoke-Trucks-Detection/main/Image/network-model.png"></p>

## 最佳批大小 Best Batch Size
<p align="center"><img src="https://raw.githubusercontent.com/f1amingo/Black-Smoke-Trucks-Detection/main/Image/best-batch-size.png"></p>

## 最佳学习率 Best Learning Rate
<p align="center"><img src="https://raw.githubusercontent.com/f1amingo/Black-Smoke-Trucks-Detection/main/Image/best-learning-rate.png"></p>


# 实验结果 Result
## 一类图片检测效果 First-class Image Result
<p align="center"><img src="https://raw.githubusercontent.com/f1amingo/Black-Smoke-Trucks-Detection/main/Image/result-first.png"></p>

## 二类图片检测效果 Second-class Image Result
<p align="center"><img src="https://raw.githubusercontent.com/f1amingo/Black-Smoke-Trucks-Detection/main/Image/result-second.png"></p>

## 误识别 Error Case
<p align="center"><img src="https://raw.githubusercontent.com/f1amingo/Black-Smoke-Trucks-Detection/main/Image/result-error.png"></p>


# 总结 Conclusion
<p align="center"><img src="https://raw.githubusercontent.com/f1amingo/Black-Smoke-Trucks-Detection/main/Image/conclusion.png"></p>
