from skimage import exposure, io
import numpy as np
import platform
from PIL import Image
from xml.dom.minidom import parse

if platform.system() == 'Windows':
    BASE_PATH = 'C:/Users/think/Desktop/VOCtemplate/VOC2019/'
else:
    BASE_PATH = '/home/ubuntu/MyFiles/VOCtemplate/VOC2019/'

IMG_PATH = BASE_PATH + 'JPEGImages/'
XML_PATH = BASE_PATH + 'Annotations/'
TXT_PATH = BASE_PATH + 'ImageSets/Main/'


def repairImgSize(file_name):
    im = Image.open(IMG_PATH + file_name)
    width = im.width
    height = im.height
    xml_file_path = XML_PATH + get_name_no_ext(file_name) + '.xml'
    dom = parse(xml_file_path)
    dom.getElementsByTagName('width')[0].childNodes[0].data = width
    dom.getElementsByTagName('height')[0].childNodes[0].data = height
    with open(xml_file_path, 'w') as f:
        f.write(dom.toxml())
    return width, height


def get_name_equalized(file_name, is_img=True):
    suffix = '_equalized'
    if is_img:
        return get_name_no_ext(file_name) + suffix + '.jpg'
    else:
        return get_name_no_ext(file_name) + suffix + '.xml'


def get_name_transpose(file_name, is_img=True):
    suffix = '_flip_LR'
    if is_img:
        return get_name_no_ext(file_name) + suffix + '.jpg'
    else:
        return get_name_no_ext(file_name) + suffix + '.xml'


def get_name_brightness(file_name, is_img=True):
    suffix = '_brightness'
    if is_img:
        return get_name_no_ext(file_name) + suffix + '.jpg'
    else:
        return get_name_no_ext(file_name) + suffix + '.xml'


def get_name_contrast(file_name, is_img=True):
    suffix = '_contrast'
    if is_img:
        return get_name_no_ext(file_name) + suffix + '.jpg'
    else:
        return get_name_no_ext(file_name) + suffix + '.xml'


def get_name_rotate(file_name, is_img=True):
    suffix = '_rotate_90'
    if is_img:
        return get_name_no_ext(file_name) + suffix + '.jpg'
    else:
        return get_name_no_ext(file_name) + suffix + '.xml'


def get_name_no_ext(file_name):
    return file_name[:file_name.index('.')]


def is_original_img(file_name):
    if len(file_name) == 10:
        return True
    return False


def is_equalize_img(file_name):
    if len(file_name) == len('000001_equalized.jpg') and file_name.find('equalized') != -1:
        return True
    return False


def is_first_second_img(file_name: str):
    if file_name.startswith('0') or file_name.startswith('1'):
        return True
    return False


def color_img_equalize_hist(full_src_path, full_dst_path):
    img = io.imread(full_src_path)
    new_img = np.zeros(img.shape, float)
    new_img[:, :, 0] = exposure.equalize_hist(img[:, :, 0])
    new_img[:, :, 1] = exposure.equalize_hist(img[:, :, 1])
    new_img[:, :, 2] = exposure.equalize_hist(img[:, :, 2])
    io.imsave(full_dst_path, new_img)
