'''
coding: utf-8
@author: WanZhijie
@create: 2023/5/14 17:43
'''

import os
import random

import pandas as pd
import numpy as np

#Author: Zhijie Wan

#utilitiy for creating new files
def newoutputfile(filename):
    file_dir = "../data"
    if not os.path.isdir(file_dir):
        os.makedirs(file_dir)
    outputfilename = "../data" + "/" + filename
    if not os.path.exists(outputfilename):
        with open(outputfilename,'w', encoding="utf-8") as f:
            f.write("")
    return outputfilename

# get 200 random repos from 2000 repos
def get_random():
    list = []
    for i in range(200):
        m = random.randint(2 + 10 * i, 11 + 10 * i)
        list.append(m)
    # print(list)
    return list

# get repos and owers from the link in csv
def geturl():
    data = pd.read_csv(r'../data/2000_sample.csv')
    path = data[['path']]
    # print(path)
    path = np.array(path)
    # print(path)
    # strArr=[]
    strArr = [''] * 200
    owner_repo = [''] * 200
    owner = [''] * 200
    repo = [''] * 200
    # list = get_random()
    # print(list)
    list = [3, 16, 27, 33, 48, 55, 63, 77, 88, 93, 110, 113, 126, 141, 146, 161, 171, 174, 188, 199, 202, 221, 226, 239,
            249, 259, 271, 280, 282, 297, 309, 313, 329, 338, 345, 356, 365, 372, 382, 394, 403, 418, 425, 441, 444,
            456, 468, 473, 488, 492, 506, 520, 525, 541, 550, 558, 569, 576, 582, 600, 602, 620, 631, 637, 643, 657,
            662, 675, 690, 701, 705, 715, 729, 739, 743, 753, 763, 772, 790, 796, 808, 820, 828, 835, 848, 852, 862,
            872, 885, 893, 906, 916, 926, 935, 944, 954, 967, 974, 983, 999, 1006, 1016, 1031, 1038, 1047, 1055, 1069,
            1078, 1088, 1100, 1106, 1116, 1130, 1134, 1143, 1158, 1163, 1176, 1189, 1199, 1205, 1221, 1223, 1237, 1247,
            1254, 1268, 1279, 1289, 1298, 1308, 1315, 1329, 1335, 1342, 1352, 1365, 1377, 1384, 1399, 1411, 1414, 1426,
            1437, 1446, 1452, 1470, 1474, 1491, 1493, 1510, 1512, 1524, 1541, 1542, 1555, 1569, 1577, 1582, 1592, 1605,
            1615, 1629, 1641, 1648, 1661, 1663, 1681, 1685, 1701, 1710, 1719, 1731, 1737, 1748, 1760, 1770, 1775, 1789,
            1792, 1810, 1819, 1827, 1840, 1842, 1857, 1863, 1872, 1890, 1901, 1907, 1913, 1924, 1932, 1945, 1956, 1962,
            1978, 1989, 1993]

    # print(len(list))
    for i in range(200):
        strArr[i] = path[list[i] - 2]
    # print(strArr[0][0])
    # strArr=np.array(strArr)
    for j in range(200):
        owner_repo[j] = strArr[j][0]
        # owner_repo[j] = strArr[j][0].replace('https://github.com/', '')
        # owner[j] = owner_repo[j].split("/")[0]
        # repo[j] = owner_repo[j].split("/")[1]
    print(owner_repo)
    # owner_repo=np.array(owner_repo)
    outputfilename = "repo_url"
    outpufile = newoutputfile(outputfilename)
    with open(outpufile, 'w+', encoding='utf-8') as f:
        f.write(str(owner_repo))

geturl()
