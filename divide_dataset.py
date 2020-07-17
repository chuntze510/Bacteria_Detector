# -*- coding: utf-8 -*-
import os
import random

trainval_percent = 1.0 #訓練加驗證集佔全部資料集比例
train_percent = 1.0 # 訓練集佔訓練加驗證集比例
xmlfilepath = 'dataset\Annotations' #標註檔路徑
txtsavepath = 'dataset\ImageSets\Main' #訓練、驗證、測試清單路徑
total_xml = os.listdir(xmlfilepath)

num=len(total_xml)
list=range(num)
tv=int(num*trainval_percent)
tr=int(tv*train_percent)
trainval= random.sample(list,tv)
train=random.sample(trainval,tr)

ftrainval = open('dataset/ImageSets/Main/trainval.txt', 'w') #指定訓練加驗證集清單檔
ftest = open('dataset/ImageSets/Main/test.txt', 'w') #指定測試資料集清單
ftrain = open('dataset/ImageSets/Main/train.txt', 'w') #指定訓練資料集清單
fval = open('dataset/ImageSets/Main/val.txt', 'w') #指定驗證資料集清單

for i  in list:
    name=total_xml[i][:-4]+'\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest .close()