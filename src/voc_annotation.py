import xml.etree.ElementTree as ET
from os import getcwd

sets=['train', 'test']

classes = ["chanel", "chanel_text"]


def convert_annotation(image_id, list_file):
    in_file = open('dataset/chanelset/annotations/%s.xml'%image_id) # Change to your annotations path
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = getcwd()

for image_set in sets:
    image_ids = open('dataset/chanelset/ids/chanel_%s.txt'%image_set).read().strip().split() # Change to your ids path
    image_ids += open('dataset/chanelset/ids/chanel_text_%s.txt'%image_set).read().strip().split()
    list_file = open('dataset/chanelset/chanel_%s.txt'%image_set, 'w') # Output path of the feeding list for training
    for image_id in image_ids:
        list_file.write('%s/dataset/chanelset/images/%s.jpg'%(wd, image_id))
        convert_annotation(image_id, list_file)
        list_file.write('\n')
    list_file.close()

