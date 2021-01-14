import re
import matplotlib.pyplot as plt
import sys

file_path_list = [
    # 'C:/Users/think/Desktop/最佳批大小/ssd_512_resnet50_v1_voc_train_8.log',
    # 'C:/Users/think/Desktop/最佳批大小/16_ssd_512_resnet50_v1_voc_train.log',
    # 'C:/Users/think/Desktop/最佳批大小/ssd_512_resnet50_v1_voc_train_24.log',
    # 'C:/Users/think/Desktop/最佳批大小/ssd_512_resnet50_v1_voc_train_32.log',
    # 'C:/Users/think/Desktop/最佳批大小/ssd_512_resnet50_v1_voc_train_40.log',
    # 'C:/Users/think/Desktop/微调实验/ssd_512_mobilenet1.0_voc_train_0.01_zero.log'
    'C:/Users/think/Desktop/毕设/网络选择实验/ssd_512_mobilenet1.0_voc_train.log',
    'C:/Users/think/Desktop/毕设/网络选择实验/ssd_512_vgg16_atrous_voc_train.log',
    'C:/Users/think/Desktop/毕设/网络选择实验/ssd_512_resnet50_v1_voc_train.log',
]

acc_list = [[], [], [], [], []]

for i, path in enumerate(file_path_list):
    with open(file_path_list[i], 'r') as f:
        line = f.readline()
        while line:
            if line.find('smoke') != -1:
                acc = float(re.findall(r"smoke=(\d+\.\d+)", line)[0])
                acc_list[i].append(acc)
            line = f.readline()

plt.plot(range(0, 25), acc_list[0][0:25], label='mobilenet1')
plt.plot(range(0, 25), acc_list[1][0:25], label='vgg16_atrous')
plt.plot(range(0, 25), acc_list[2][0:25], label='resnet50_v1')

# plt.plot(range(0, last_epoch), acc_list[0][:last_epoch], label='batch size 8')
# plt.plot(range(0, last_epoch), acc_list[1][:last_epoch], label='batch size 16')
# plt.plot(range(0, last_epoch), acc_list[2][:last_epoch], label='batch size 24')
# plt.plot(range(0, last_epoch), acc_list[3][:last_epoch], label='batch size 32')
# plt.plot(range(0, last_epoch), acc_list[4][:last_epoch], label='batch size 40')

# plt.plot(range(0, len(acc_list[0])), acc_list[0], label='mobilenet1')
# plt.plot(range(0, len(acc_list[1])), acc_list[1], label='vgg16_atrous')
# plt.plot(range(0, len(acc_list[2])), acc_list[2], label='resnet50_v1')
plt.legend()
plt.xlabel('epoch(%d batches/epoch, batch size=%d)' % (132, 16))
plt.ylabel('mAP')
# plt.xticks(range(0, len(acc_list[0])))
plt.show()
