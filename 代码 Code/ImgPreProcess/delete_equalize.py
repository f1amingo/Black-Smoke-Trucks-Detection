import os
import utils

img_count = 0
xml_count = 0

for file_name in os.listdir(utils.IMG_PATH):
    if file_name.find('equalize') != -1:
        os.remove(utils.IMG_PATH + file_name)
        img_count += 1

for file_name in os.listdir(utils.XML_PATH):
    if file_name.find('equalize') != -1:
        os.remove(utils.XML_PATH + file_name)
        xml_count += 1

print('删除图片：%d，删除xml：%d' % (img_count, xml_count))
