import re
import matplotlib.pyplot as plt

import re
import matplotlib.pyplot as plt


def parse_loss(file_path):
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
        batch_per_epoch += 1
        epoch_list = []
        this_epoch_tick = 0.0
        for i in range(0, len(cross_entropy_list)):
            epoch_list.append(this_epoch_tick)
            this_epoch_tick += 1 / batch_per_epoch
    return cross_entropy_list, smoothL1_list, epoch_list


file_path = [
    'C:/Users/think/Desktop/最佳学习率/16_0.001_ssd_512_resnet50_v1_voc_train.log',
    'C:/Users/think/Desktop/最佳学习率/16_0.0001_ssd_512_resnet50_v1_voc_train.log',
    'C:/Users/think/Desktop/最佳学习率/16_0.00001_ssd_512_resnet50_v1_voc_train.log',
]

error_case = [
    'C:/Users/think/Desktop/最佳学习率/16_0.1_ssd_512_resnet50_v1_voc_train.log',
    'C:/Users/think/Desktop/最佳学习率/16_0.01_ssd_512_resnet50_v1_voc_train.log',
]

loss_list = [parse_loss(file_path[0]), parse_loss(file_path[1]), parse_loss(file_path[2])]

# plt.plot(loss_list[0][2], loss_list[0][0], label='0.001')
# plt.plot(loss_list[0][2], loss_list[1][0], label='0.0001')
# plt.plot(loss_list[0][2], loss_list[2][0], label='0.00001')
# plt.ylabel('cross entropy loss')

# plt.plot(loss_list[0][2], loss_list[0][1], label='0.001')
# plt.plot(loss_list[0][2], loss_list[1][1], label='0.0001')
# plt.plot(loss_list[0][2], loss_list[2][1], label='0.00001')
# plt.ylabel('smoothL1 loss')

error_case_1 = parse_loss(error_case[0])
error_case_2 = parse_loss(error_case[1])
# plt.plot(error_case_1[2], error_case_1[0], label='cross entropy loss')
# plt.plot(error_case_1[2], error_case_1[1], label='smoothL1 loss')
plt.plot(error_case_2[2], error_case_2[0], label='cross entropy loss')
plt.plot(error_case_2[2], error_case_2[1], label='smoothL1 loss')
plt.ylabel('loss')
plt.xlabel('epoch')

plt.legend()

plt.show()
