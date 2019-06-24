# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:14:18 2019
@author: TinCya
"""
# import numpy as np
# from PIL import Image
# import matplotlib.pyplot as plt

# def fib( n ) :
# 	a, b = 0, 1
# 	while a < n:
# 		# python 2
# 		print a,
# 		a, b = b, a + b
# fib(2000)

#i = Image.open('maskmy.jpg')
#iar = np.asarray(i)

#plt.imshow(iar)
#print(iar)
#plt.show()

import numpy as np
import math
adoimg = np.array([[1,2,3],[4,5,6],[8,8,8]])

adnimg = np.array([
		[2,2,2,2,2],
		[4,5,6,4,4],
		[6,6,6,6,6],
		[8,8,8,8,8]])
adnimg[1:3,2:4]=0
print(adnimg)
print(1 and 5)

#print(adoimg)
#print(adnimg)

s=np.sum(np.where(adoimg>0,1,0))
# df = adoimg-adnimg
# df = np.sum( (adoimg-adnimg)**2 )

