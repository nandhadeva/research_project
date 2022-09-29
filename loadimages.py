from PIL import Image
import glob
import os
import csv
import numpy as np


def load():
    path = 'image\*.jpg'
    path1 = 'image'
    image_list = []
    for filename in glob.glob(path):
        im = Image.open(filename)
        image_list.append(np.asarray(im).shape)
    image_names = []
    for i in os.listdir(path1):
        if "jpg" in i:
            image_names.append(i.split(".")[0])
    return image_names, image_list


def split(image_names, image_list):
    headnames = ["Images_Name", "NumericData"]
    image_data = []
    list = []
    for i in range(len(image_names)):
        val = []
        for k in range(1):
            val.append(image_names[i])
            val.append(image_list[i])
        list.append(val)
    with open("dataset.csv", "w", encoding='UTF8', newline="") as f:
        s = csv.writer(f)
        s.writerow(headnames)
        s.writerows(list)


t1, t2 = load()
split(t1, t2)
