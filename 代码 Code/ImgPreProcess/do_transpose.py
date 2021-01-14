import os
import utils
from PIL import Image
from xml.dom.minidom import parse


def makeAnnotationXML(file_name):
    xml_file_path = utils.XML_PATH + utils.get_name_no_ext(file_name) + '.xml'
    dom = parse(xml_file_path)
    # 修复高宽
    width = int(dom.getElementsByTagName('width')[0].childNodes[0].data)
    height = int(dom.getElementsByTagName('height')[0].childNodes[0].data)
    if width == 0 or height == 0:
        width, height = utils.repairImgSize(file_name)
    # 改文件名
    dom.getElementsByTagName('filename')[0].childNodes[0].data = utils.get_name_transpose(file_name)
    obj_list = dom.getElementsByTagName('object')
    for obj in obj_list:
        xmin = obj.getElementsByTagName('xmin')[0].childNodes[0].data
        ymin = obj.getElementsByTagName('ymin')[0].childNodes[0].data
        xmax = obj.getElementsByTagName('xmax')[0].childNodes[0].data
        ymax = obj.getElementsByTagName('ymax')[0].childNodes[0].data
        xmin_hat = width - int(xmax)
        if xmin_hat == 0:
            xmin_hat = 1
        xmax_hat = width - int(xmin)
        if xmin_hat == 0:
            xmax_hat = 1
        obj.getElementsByTagName('xmin')[0].childNodes[0].data = xmin_hat
        obj.getElementsByTagName('xmax')[0].childNodes[0].data = xmax_hat
    with open(utils.XML_PATH + utils.get_name_transpose(file_name, False), 'w') as f:
        f.write(dom.toxml())


count = 0
for file_name in os.listdir(utils.IMG_PATH):
    if utils.is_original_img(file_name) and utils.is_first_second_img(file_name):
        print(file_name)
        two_file_name = [
            file_name,
            utils.get_name_equalized(file_name)
        ]
        mod = count % 2
        count += 1
        im = Image.open(utils.IMG_PATH + two_file_name[mod])
        out = im.transpose(Image.FLIP_LEFT_RIGHT)
        out.save(utils.IMG_PATH + utils.get_name_transpose(two_file_name[mod]))
        makeAnnotationXML(two_file_name[mod])
