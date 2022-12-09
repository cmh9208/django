# services DB없는 공간






from __future__ import print_function
#%matplotlib inline
import argparse
import os
import random
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.backends.cudnn as cudnn
import torch.optim as optim
import torch.utils.data
import torchvision.datasets as dset
import torchvision.transforms as transforms
import torchvision.utils as vutils
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML
from tqdm import tqdm

# 1.번 시드(더미값) 랜덤 시 동일값 주기 print("Random Seed: ", manualSeed)
class DcGan(object):
    def __init__(self):
        pass

crime_menu = {
    "1" : lambda t: t.spec(),
    "2" : lambda t: t.save_police_pos(),
    "3" : lambda t: t.save_cctv_pop(),
    "4" : lambda t: t.save_police_norm(),
    "5" : lambda t: t.folium_example(),
    "6" : lambda t: t.target(),
    "7" : lambda t: t.partition()
}

manualSeed = 999
if __name__ == '__main__':
    menu = input()
    while True:
        if menu == '0':
            print("종료")
            break
        elif menu == '1':
            print()
            print("### 시드값 출력 ###")
            print("Random Seed: ", manualSeed)
         else:
             print()

