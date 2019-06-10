# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:14:18 2019
@author: TinCya
"""
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def fib( n ) :
	a, b = 0, 1
	while a < n:
		# python 2
		print a,
		a, b = b, a + b
fib(2000)

#i = Image.open('maskmy.jpg')
#iar = np.asarray(i)

#plt.imshow(iar)
#print(iar)
#plt.show()


