import os
import utils
import random

train_txt_path = utils.TXT_PATH + 'train.txt'
test_txt_path = utils.TXT_PATH + 'test.txt'

train0_txt_path = utils.TXT_PATH + 'train0.txt'
test0_txt_path = utils.TXT_PATH + 'test0.txt'

train1_txt_path = utils.TXT_PATH + 'train1.txt'
test1_txt_path = utils.TXT_PATH + 'test1.txt'

dir_list = os.listdir(utils.IMG_PATH)
test_list = []
for i in range(0, 500):
    while True:
        this_file = random.choice(dir_list)
        if this_file not in test_list:
            test_list.append(this_file)
            break

test_list.sort()

with open(test_txt_path, 'w') as f:
    for file_name in test_list:
        f.write(utils.get_name_no_ext(file_name) + '\n')

with open(train_txt_path, 'w') as f:
    for file_name in dir_list:
        if file_name not in test_list:
            f.write(utils.get_name_no_ext(file_name) + '\n')

# with open(train0_txt_path, 'w') as f:
#     for file_name in os.listdir(utils.IMG_PATH):
#         if utils.is_original_img(file_name):
#             line = utils.get_name_no_ext(file_name)
#             f.write(line + '\n')
#
# with open(test0_txt_path, 'w') as f:
#     for file_name in os.listdir(utils.IMG_PATH):
#         if utils.is_original_img(file_name):
#             name_no_ext = utils.get_name_no_ext(file_name)
#             if name_no_ext.startswith('0'):
#                 f.write(name_no_ext + '\n')
#
# with open(train1_txt_path, 'w') as f:
#     for file_name in os.listdir(utils.IMG_PATH):
#         if file_name.find('equalized') != -1:
#             line = utils.get_name_no_ext(file_name)
#             f.write(line + '\n')
#
# with open(test1_txt_path, 'w') as f:
#     for file_name in os.listdir(utils.IMG_PATH):
#         if file_name.find('equalized') != -1 and file_name.startswith('0'):
#             line = utils.get_name_no_ext(file_name)
#             f.write(line + '\n')
