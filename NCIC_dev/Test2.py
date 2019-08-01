# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:14:18 2019
@author: TinCya
"""
# import matplotlib.pyplot as plt
# from skimage import data, img_as_float
# from skimage.measure import compare_ssim as ssim
# from skimage.measure import compare_mse as cmse

import numpy as np
import cv2
# ---------- OCR
# try:
# 	doimg = cv2.imread(".\\A2\\BL_273_rowno_262_20190715-15-57-59.png")
# 	dnimg = cv2.imread(".\\A1\\BL_492_rowno_262_20190318-11-47-16.png")
# except IOError:
# 	print("Can not open")
# # adoi=cv2.cvtColor(doimg, cv2.COLOR_BGR2GRAY)
# # adni=cv2.cvtColor(dnimg, cv2.COLOR_BGR2GRAY)
# adoi = np.trunc(np.average(doimg, axis=2)).astype(int)
# adni = np.trunc(np.average(dnimg, axis=2)).astype(int)

# import pytesseract
# tdo=pytesseract.image_to_string(adoi)
# tdn=pytesseract.image_to_string(adni)
# fwpb= open("ao.txt","w+")
# fwpb.write(tdo)
# fwpb.close()
# fwpb= open("an.txt","w+")
# fwpb.write(tdn)
# fwpb.close()

# -------------------DELETE
a=np.array([[1,2,3],[4,5,4],[5,5,5]])
b=np.array([[1,2,3],[4,5,4],[5,5,5],[6,8,6]])
# a=np.insert(a,(range(3,4)),[11],0)
b[3:4,:]=0
print(a)
print(not ".csv".endswith("csv"))
# CSV-----------
docsv = open("RESULT_OUT_A2.csv","r")
rl=docsv.read().splitlines()
print(rl)
a1=set([1,2,3,1,4])
a2=set([1,2,3,1,5])
a3=a1.difference(a2)

print(a3)

# while (rl!="") :
# 	rl=docsv.readline()
# 	print(1,rl,end="")


# av=np.average(a,axis=1)
# avd=np.delete(av,1,0)
# print(avd)

# adoimg=np.delete(a,1,0)
# print(adoimg)



# cv2.imwrite(".\\doimg.png",adoi)
# cv2.imwrite(".\\dnimg.png",adni)

# oimg = img_as_float(adoi)
# nimg = img_as_float(adni)

# rmse = cmse(oimg, nimg)
# rssim = ssim(oimg, nimg)
# print(rmse,rssim)

# exit()
# -------------

# img = img_as_float(data.camera())

# rows, cols = img.shape

# noise = np.ones_like(img) * 0.2 * (img.max() - img.min())
# noise[np.random.random(size=noise.shape) > 0.5] *= -1

# def mse(x, y):
#     return np.linalg.norm(x - y)

# img_noise = img + noise
# img_const = img + abs(noise)

# fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(10, 4),
#                          sharex=True, sharey=True)
# ax = axes.ravel()

# mse_none = mse(img, img)
# ssim_none = ssim(img, img, data_range=img.max() - img.min())

# mse_noise = mse(img, img_noise)
# ssim_noise = ssim(img, img_noise,
#                   data_range=img_noise.max() - img_noise.min())

# mse_const = mse(img, img_const)
# ssim_const = ssim(img, img_const,
#                   data_range=img_const.max() - img_const.min())

# label = 'MSE: {:.2f}, SSIM: {:.2f}'

# ax[0].imshow(img, cmap=plt.cm.gray, vmin=0, vmax=1)
# ax[0].set_xlabel(label.format(mse_none, ssim_none))
# ax[0].set_title('Original image')

# ax[1].imshow(img_noise, cmap=plt.cm.gray, vmin=0, vmax=1)
# ax[1].set_xlabel(label.format(mse_noise, ssim_noise))
# ax[1].set_title('Image with noise')

# ax[2].imshow(img_const, cmap=plt.cm.gray, vmin=0, vmax=1)
# ax[2].set_xlabel(label.format(mse_const, ssim_const))
# ax[2].set_title('Image plus constant')

# plt.tight_layout()
# plt.show()