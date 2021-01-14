import os
import utils
from xml.dom.minidom import parse
from PIL import Image, ImageEnhance

count = 0
for file_name in os.listdir(utils.IMG_PATH):
    if utils.is_original_img(file_name) and utils.is_first_second_img(file_name):
        two_file_name = [
            file_name,
            utils.get_name_equalized(file_name)
        ]
        mod = count % 2
        count += 1
        im = Image.open(utils.IMG_PATH + two_file_name[mod])
        # 亮度变化
        out = ImageEnhance.Contrast(im).enhance(0.5)
        out.save(utils.IMG_PATH + utils.get_name_contrast(two_file_name[mod]))
        # 生成xml
        src_xml_path = utils.XML_PATH + utils.get_name_no_ext(file_name) + '.xml'
        dom = parse(src_xml_path)
        dom.getElementsByTagName('filename')[0].childNodes[0].data = utils.get_name_contrast(two_file_name[mod])
        dom.getElementsByTagName('path')[0].childNodes[0].data = utils.IMG_PATH + utils.get_name_contrast(
            two_file_name[mod])
        with open(utils.XML_PATH + utils.get_name_contrast(two_file_name[mod], False), 'w') as f:
            f.write(dom.toxml())
