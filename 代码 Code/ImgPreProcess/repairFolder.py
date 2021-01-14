import os
import utils
from xml.dom.minidom import parse

for file_name in os.listdir(utils.XML_PATH):
    print(file_name)
    dom = parse(utils.XML_PATH + file_name)
    dom.getElementsByTagName('folder')[0].childNodes[0].data = 'JPEGImages'
    dom.getElementsByTagName('path')[0].childNodes[0].data = 'JPEGImages/' + utils.get_name_no_ext(file_name) + '.jpg'
    with open(utils.XML_PATH + file_name, 'w') as f:
        f.write(dom.toxml())
