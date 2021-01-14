import os
import utils
from xml.dom.minidom import parse

for file_name in os.listdir(utils.IMG_PATH):
    if utils.is_original_img(file_name) and utils.is_first_second_img(file_name):
        print(file_name)
        # 均衡化图片
        utils.color_img_equalize_hist(utils.IMG_PATH + file_name, utils.IMG_PATH + utils.get_name_equalized(file_name))
        # 生成xml
        src_xml_path = utils.XML_PATH + utils.get_name_no_ext(file_name) + '.xml'
        dom = parse(src_xml_path)
        dom.getElementsByTagName('filename')[0].childNodes[0].data = utils.get_name_equalized(file_name)
        dom.getElementsByTagName('path')[0].childNodes[0].data = utils.IMG_PATH + utils.get_name_equalized(file_name)
        with open(utils.XML_PATH + utils.get_name_equalized(file_name, False), 'w') as f:
            f.write(dom.toxml())
