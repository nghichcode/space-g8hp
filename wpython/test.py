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
#import math
#adoimg = np.array([[1,2,3],[4,5,6],[8,8,8]])
adoimg = np.array([
		[1,9,3,4,5,6],
		[6,7,8,9,0,1],
		[1,2,3,4,5,2],
		[8,8,8,8,8,3]])

adnimg = np.array([
		[1,2,3,4,5,6],
		[6,7,8,9,0,1],
		[1,2,3,4,5,2],
		[8,8,8,8,8,3]])
cc = np.subtract(adnimg,adoimg)

w=3;h=2;
adnimg = np.reshape(adnimg, (-1,w) )
adnimg = np.sum(adnimg, axis=1)
adnimg = np.reshape(adnimg, (-1,int(6/w)) )
atnimg = adnimg.T
atnimg = np.reshape(atnimg, (-1,h) )
atnimg = np.sum(atnimg, axis=1)
atnimg = np.reshape(atnimg, (-1,int(4/h)) )

#ndoimg = adoimg[0:IWIDTH,0:IHEIGHT]
#ndoimg = np.reshape(ndoimg, ())
#ndnimg = adnimg[0:IWIDTH,0:IHEIGHT]

np.
print(atnimg)
print(0.9>2)
for r in range(10,0,-1):
	print(r)
#s=np.sum(np.where(adoimg>0,1,0))
#
#def cc(a, *kw):
#	print(a)
#	g,h=kw
#	print(kw)
#cc(123,3,5)
# df = adoimg-adnimg
# df = np.sum( (adoimg-adnimg)**2 )

