import utils
import os

first_count = 0
second_count = 0
third_count = 0

equalized_count = 0
flip_count = 0
brightness_count = 0
contrast_count = 0

for file_name in os.listdir(utils.IMG_PATH):
    if utils.is_original_img(file_name):
        if file_name.startswith('0'):
            first_count += 1
        elif file_name.startswith('1'):
            second_count += 1
        elif file_name.startswith('2'):
            third_count += 1
    else:
        if len(file_name) == 20:
            equalized_count += 1
        elif file_name.find('flip') != -1:
            flip_count += 1
        elif file_name.find('brightness') != -1:
            brightness_count += 1
        elif file_name.find('contrast') != -1:
            contrast_count += 1

print('原始图片总数：%d' % (first_count + second_count + third_count))
print('original 一类图片：%d，二类图片：%d，三类图片：%d' % (first_count, second_count, third_count))
print('equalized: %d, flip: %d, brightness: %d, contrast: %d' % (
    equalized_count, flip_count, brightness_count, contrast_count))
