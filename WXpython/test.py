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
# adoimg = np.array([
# 		[1,9,3,4,5,6],
# 		[6,7,8,9,0,1],
# 		[1,2,3,4,5,2],
# 		[8,8,8,8,8,3]])

# adnimg = np.array([
# 		[1,2,3,4,5,6],
# 		[6,7,8,9,0,1],
# 		[1,2,3,4,5,2],
# 		[8,8,8,8,8,3]])
# cc = np.subtract(adnimg,adoimg)

# w=3;h=2;
# adnimg = np.reshape(adnimg, (-1,w) )
# adnimg = np.sum(adnimg, axis=1)
# adnimg = np.reshape(adnimg, (-1,int(6/w)) )
# atnimg = adnimg.T
# atnimg = np.reshape(atnimg, (-1,h) )
# atnimg = np.sum(atnimg, axis=1)
# atnimg = np.reshape(atnimg, (-1,int(4/h)) )

# print(atnimg)

ard=np.array([[1,2,3],[0,0,0],[9,9,9],[1,1,2],[4,5,6],[0,0,0],[8,9,0]])
# nwd=np.where(ard>0)
# nwd=np.delete(ard,[1,3],0)
nav=np.average(ard,axis=1)
tsd=np.argwhere(nav<=1).reshape(-1)
nwd=np.delete(ard,tsd,0)
nav=np.delete(nav,tsd)

print(nwd)
print(nav)

# nwd=np.delete(ard,np.argwhere(nav<=1))
# nwd=np.argwhere(ard>0)
# print(nwd)

# dfs = [
# 	["DI-POD_Phase 1_TestPattern_3_220_rowno_15_20190318-11-19-58.png","DI-POD_Phase 1_TestPattern_3_10_rowno_100_20190523-19-05-57.png"],
# 	["DI-POD_Phase 1_TestPattern_3_221_rowno_18_20190318-11-20-03.png","DI-POD_Phase 1_TestPattern_3_11_rowno_112_20190523-19-06-04.png"],
# 	["DI-POD_Phase 1_TestPattern_3_222_rowno_25_20190318-11-20-07.png","DI-POD_Phase 1_TestPattern_3_12_rowno_137_20190523-19-06-22.png"],
# 	["DI-POD_Phase 1_TestPattern_3_223_rowno_28_20190318-11-20-08.png","DI-POD_Phase 1_TestPattern_3_13_rowno_149_20190523-19-06-29.png"],
# 	["DI-POD_Phase 1_TestPattern_3_224_rowno_41_20190318-11-20-15.png","DI-POD_Phase 1_TestPattern_3_14_rowno_165_20190523-19-06-40.png"],
# 	["DI-POD_Phase 1_TestPattern_3_225_rowno_50_20190318-11-20-19.png","DI-POD_Phase 1_TestPattern_3_15_rowno_179_20190523-19-06-50.png"],
# 	["DI-POD_Phase 1_TestPattern_3_226_rowno_59_20190318-11-20-23.png","DI-POD_Phase 1_TestPattern_3_16_rowno_193_20190523-19-06-57.png"],
# 	["DI-POD_Phase 1_TestPattern_3_227_rowno_68_20190318-11-20-28.png","DI-POD_Phase 1_TestPattern_3_17_rowno_218_20190523-19-07-15.png"],
# 	["DI-POD_Phase 1_TestPattern_3_228_rowno_76_20190318-11-20-33.png","DI-POD_Phase 1_TestPattern_3_18_rowno_230_20190523-19-07-22.png"],
# 	["DI-POD_Phase 1_TestPattern_3_229_rowno_100_20190318-11-20-51.png","DI-POD_Phase 1_TestPattern_3_19_rowno_249_20190523-19-07-38.png"],
# 	["DI-POD_Phase 1_TestPattern_3_230_rowno_112_20190318-11-20-57.png","DI-POD_Phase 1_TestPattern_3_1_rowno_15_20190523-19-04-58.png"]
# ];

# dfsa = []
# dfsb = []
# for i,ai in enumerate(dfs):
# 	dfsa.append(ai[0])
# 	dfsb.append(ai[1])

# dfsa.sort(key=lambda f:int(filter(str.isdigit, f)) )
# dfsb.sort(key=lambda f:int(filter(str.isdigit, f)) )

# print("-")
# import re
# dfsb.sort(key=lambda vr:[int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', vr) ] )
# bar = [ c for c in re.split('([0-9]+)',dfsb[0]) ]
# print(bar)
# print("-")

# for i in range(len(dfsb)):
# 	print(" ",dfsa[i], dfsb[i])

#ndoimg = adoimg[0:IWIDTH,0:IHEIGHT]
#ndoimg = np.reshape(ndoimg, ())
#ndnimg = adnimg[0:IWIDTH,0:IHEIGHT]

#print(atnimg)
#print(0.9>2)
#for r in range(10,0,-1):
#	print(r)
#s=np.sum(np.where(adoimg>0,1,0))
#
#def cc(a, *kw):
#	print(a)
#	g,h=kw
#	print(kw)
#cc(123,3,5)
# df = adoimg-adnimg
# df = np.sum( (adoimg-adnimg)**2 )

# -------------<
# import os

# print("--------------")
# cfo = u"D:\\ReactJS\\public\\compare-image\\CPH\\OSimple"
# cfn = u"D:\\ReactJS\\public\\compare-image\\CPH\\NSimple"

# outcf=cfo[:cfo.rfind("\\")]
# print(outcf)

# owcfo=os.walk(cfo)
# owcfn=os.walk(cfn)
# while (True):
# 	try:
# 		nocfo = next(owcfo);
# 		nocfn = next(owcfn);
# 		imsfo=sorted(nocfo[2], key=lambda vr:[int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', vr) ] )
# 		imsfn=sorted(nocfn[2], key=lambda vr:[int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', vr) ] )
# 		print(imsfo)
# 		print(imsfo)
# 	except StopIteration as e:
# 		break;

# mna = [1,2,3,45,56,7,2]
# mnb = mna[0:99] 
# print(mnb)
# --------->
# for r, d, f in owo:
# 	# print(r,f,d)
# 	print("--s--")
# 	print(r.replace(cfo,cfn),r,f)
# 	print("--e--")



