import cv2
import numpy as np
import os

path_true = "img_noise/1/"
path_false = "image/1ac1e8a095df4611af387d9934799251/dev/0/"
patha = "lvb/"


def getzs(path):
    image = cv2.imread(path, 0)  # 0表示以灰度模式读取图像
    # 计算图像的标准差
    std_deviation = np.std(image)
    # 根据标准差的阈值来判断是否有噪声
    threshold = 35  # 调整此阈值以适应你的图像
    print(std_deviation)
    if std_deviation > threshold:
        print("图片有噪声")
    else:
        print("图片没有噪声")
    print()


def forpath(path):
    pathlist = os.listdir(path)
    for i in pathlist:
        try:
            path_one = path + i
            print(path_one)
            getzs(path_one)
        except:
            continue


forpath(patha)
