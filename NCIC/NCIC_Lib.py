import os
import numpy as np
#from PIL import Image
#import matplotlib.pyplot as plt
from datetime import datetime
import shutil
import math
import cv2
# Task : save dir, response to global

def compareIMG(cf, ioim ,inim, w=1, h=1, ipsx=0, ipsy=0, ipex=0, ipey=0) :
	if ( (ipsx>ipex and ipex!=-1) or (ipsy>ipey and ipey!=-1) ): return "Err <>"
	print(1,datetime.now())
	try:
		doimg = cv2.imread(cf+ioim)
		dnimg = cv2.imread(cf+inim)
	except IOError:
		print("Can not open")
		return
	print(2,datetime.now())
	match=True

	adoimg = cv2.cvtColor(doimg, cv2.COLOR_BGR2GRAY)
	adnimg = cv2.cvtColor(dnimg, cv2.COLOR_BGR2GRAY)
	if (len(adoimg)<len(adnimg) or len(adoimg[0])<len(adnimg[0]) ): return "Err L"
	IHEIGHT=len(adoimg)
	IWIDTH= len(adoimg[0])
	if (ipex==-1): ipex=IWIDTH
	if (ipey==-1): ipey=IHEIGHT
	adoimg[ipsy:ipey,ipsx:ipex]=0
	adnimg[ipsy:ipey,ipsx:ipex]=0

	asf = np.absolute(np.subtract( np.array(adoimg,np.int8),np.array(adnimg,np.int8) ))
	adf = np.where(asf>3,1,0)
	sdf = np.sum(adf)
	glf = (sdf/(IWIDTH*IHEIGHT-(ipex-ipsx)*(ipey-ipsy)))*100
	adoimg=np.where(adf!=0,222,adoimg)
	adnimg=np.where(adf!=0,222,adnimg)
	print( glf, "% diff" )
	print(3,datetime.now())

	cv2.imwrite('io.jpg',adoimg)
	cv2.imwrite('in.jpg',adnimg)
	return
	# DIFF - R
	print(3,datetime.now())
	GEP=0;
	for i in range(0,(IHEIGHT-h),h):
		for j in range(0,(IWIDTH-w),w):
			if(i+h>=IHEIGHT or w+j>=IWIDTH): print(hi,wj);break;

			eper=0; para=-1;
			for hi in range(i,(i+h)):
				for wj in range(j,(j+w)):
					if ( (wj>=ipsx and wj<ipex) and (hi>=ipsy and hi<ipey) ): continue;
					lpara = abs(int(adoimg[hi,wj]) - int(adnimg[hi,wj]))
					GEP+=(lpara)
					if ( lpara!=0 and lpara!=para ) :
						eper+=1; para=lpara if (para==-1) else -1;
			# GEP+=eper
			# if (eper/(h*w)>(50/100)):
			# 	match=False
			# 	for hi in range(i,(i+h)):
			# 		for wj in range(j,(j+w)):
			# 				adoimg[hi,wj]=[255,0,0];adnimg[hi,wj]=[255,0,0];
	print(4,datetime.now())
	print(match,cf,GEP,"DIFFERENT "+str( math.trunc((GEP*10000)/(IWIDTH*IHEIGHT))/100 )+"%")

	# simg = Image.fromarray(adoimg)
	# simg.save('io.jpg')
	# simg.save(cf+"_OUT"+ioim)
	# simg = Image.fromarray(adnimg)
	# simg.save('in.jpg')
	# simg.save(cf+"_OUT"+inim)

	cv2.imwrite('io.jpg',adoimg)
	cv2.imwrite('in.jpg',adnimg)
	print(5,datetime.now())
	# plt.imshow(adoimg)
	# plt.show()
	# plt.imshow(adnimg)
	# plt.show()
	return match

def get_data(cf, btn, w=0, h=0, ipsx=0, ipsy=0, ipex=0, ipey=0) :
	print('gs',datetime.now())

	try:
		shutil.rmtree(cf+"_OUT")
	except FileNotFoundError as fnf:
		print(fnf)
	except OSError as ose:
		print(ose)

	ncdir = []
	for r, d, f in os.walk(cf): ncdir=d; break;
	if (len(ncdir) != 2): return "Child Folders != 2 folders"

	dofs = "\\"+ncdir[1]; dnfs = "\\"+ncdir[0];
	infs=[]; iofs=[];
	for r, d, f in os.walk(cf+dofs): iofs=d; break;
	for r, d, f in os.walk(cf+dnfs): infs=d; break;
	if (len(iofs) != len(infs)): return "Folders To Compare is Different length"
	for i in range(len(iofs)):
		if (iofs[i]!=infs[i]): return "Folders To Compare are Different Name"
		diofs=dofs+"\\"+iofs[i];dinfs=dnfs+"\\"+infs[i];
		os.makedirs(cf+"_OUT"+diofs);os.makedirs(cf+"_OUT"+dinfs)
		imofs=[];imnfs=[]
		for r, d, f in os.walk(cf+diofs): imofs=f;odi=r; break;
		for r, d, f in os.walk(cf+dinfs): imnfs=f;ndi=r; break;
		imofs=sorted(imofs); imnfs=sorted(imnfs);
		
		if (len(imofs) != len(imnfs)): return "Image items To Compare are Different Length"
		for j in range(len(imofs)):
			# btn.SetLabel(str(j)+"/"+str(len(imofs))+" of "+str(i)+"/"+str(len(iofs)))
			print('-------------------------------')
			print('s',datetime.now())
			print('----',diofs+"\\"+imofs[j],'----')
			compareIMG(cf,diofs+"\\"+imofs[j],dinfs+"\\"+imnfs[j], 2, 2,ipex=-1,ipey=30)
			print('e',datetime.now())
			break;
		break;

	# btn.SetLabel("DONE!")
	return "OK"

COMPARE_FOLD = u".\\CompareFolder"
print(get_data(COMPARE_FOLD,'btn'))