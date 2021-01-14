import re
import matplotlib.pyplot as plt
import sys


def sub_plot(file_path):
    last_epoch = 100
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    print('file_path: ' + file_path)
    epoch_list = []
    cross_entropy_list = []
    smoothL1_list = []
    epoch_num = 0
    batch_per_epoch = 0
    batch_size = 0
    with open(file_path, 'r') as f:
        line = f.readline()
        while line:
            if line.find('batch_size') != -1:
                batch_size = int(re.findall(r"batch_size=(\d+)", line)[0])
            elif line.find('Epoch') != -1 and line.find('Batch') != -1:
                this_epoch = int(re.findall(r"Epoch (\d+)", line)[0])
                if this_epoch > last_epoch:
                    break
                this_batch = int(re.findall(r"Batch (\d+)", line)[0])
                str_CE = re.findall(r"CrossEntropy=(\d+\.\d+)", line)
                str_l1 = re.findall(r"SmoothL1=(\d+\.\d+)", line)
                cross_entropy_list.append(float(str_CE[0]))
                smoothL1_list.append(float(str_l1[0]))
                if epoch_num < this_epoch:
                    epoch_num = this_epoch
                if batch_per_epoch < this_batch:
                    batch_per_epoch = this_batch
            line = f.readline()
    print('epoch_num: %d, batch_per_epoch: %d, batch_size: %d' % (epoch_num, batch_per_epoch, batch_size))
    batch_per_epoch += 1
    epoch_list = []
    this_epoch_tick = 0.0
    for i in range(0, len(cross_entropy_list)):
        epoch_list.append(this_epoch_tick)
        this_epoch_tick += 1 / batch_per_epoch
    plt.plot(epoch_list, cross_entropy_list, label='cross entropy')
    plt.plot(epoch_list, smoothL1_list, label='smoothL1')
    # plt.xticks(range(0, epoch_num))
    plt.ylabel('loss')
    # plt.xlabel('epoch(%d batches/epoch, batch size=%d)' % (batch_per_epoch, batch_size))
    plt.legend()


file_path = [
    # 'C:/Users/think/Desktop/网络选择实验/ssd_512_mobilenet1.0_voc_train.log',
    # 'C:/Users/think/Desktop/网络选择实验/ssd_512_vgg16_atrous_voc_train.log',
    # 'C:/Users/think/Desktop/网络选择实验/ssd_512_resnet50_v1_voc_train.log',
]
# plt.subplot(311)
# plt.xlabel('mobilenet1')
# sub_plot(file_path[0])
#
# plt.subplot(312)
# plt.xlabel('vgg16_atrous')
# sub_plot(file_path[1])
#
# plt.subplot(313)
# plt.xlabel('resnet50_v1')
# sub_plot(file_path[2])
sub_plot(file_path[0])
plt.xlabel('epoch')
plt.show()
