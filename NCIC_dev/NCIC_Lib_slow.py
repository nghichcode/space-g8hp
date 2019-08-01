import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from datetime import datetime
import shutil
import math
# Task : save dir, response to global

def compareIMG(cf, ioim ,inim, w=1, h=1, ipsx=0, ipsy=0, ipex=0, ipey=0) :
	if (ipsx>ipex or ipsy>ipey): return "Err <>"
	print(1,datetime.now())
	try:
		doimg = Image.open(cf+ioim)
		dnimg = Image.open(cf+inim)
	except IOError:
		print("Can not open")
		return "Cant open"
	match=True

	adoimg = np.array(doimg)
	adnimg = np.array(dnimg)
	IHEIGHT=len(adoimg) if (len(adoimg)<len(adnimg)) else len(adnimg)
	IWIDTH= len(adoimg[0]) if (len(adoimg[0])<len(adnimg[0])) else len(adnimg[0])
	omColor={};nmColor={};

	print(2,datetime.now())
	# for i in range(IHEIGHT):
	# 	for j in range(IWIDTH):
	# 		if ( (j>=ipsx and j<ipex) and (i>=ipsy and i<ipey) ): avg=250; # Remove Time - WHITE
	# 		else : avg = (int(adoimg[i,j,0]) + int(adoimg[i,j,1]) + int(adoimg[i,j,2]))//3;
	# 		adoimg[i,j]=[avg,avg,avg]
	# 		omColor[avg] = omColor[avg]+1 if (avg in omColor) else 1
	# 		if ( (j>=ipsx and j<ipex) and (i>=ipsy and i<ipey) ): avg=250; # Remove Time - WHITE
	# 		else : avg = (int(adnimg[i,j,0]) + int(adnimg[i,j,1]) + int(adnimg[i,j,2]))//3;
	# 		adnimg[i,j]=[avg,avg,avg]
	# 		nmColor[avg] = nmColor[avg]+1 if (avg in nmColor) else 1

	print(3,datetime.now())
	# OBG=0;NBG=0;MXO=0;MXN=0;
	# for k,v in omColor.items():
	# 	if (v>MXO): OBG=k;MXO=v;
	# for k,v in nmColor.items():
	# 	if (v>MXN): NBG=k;MXN=v;
	# SET-BGCOLOR - G
	# DIFF - R
	print(4,datetime.now())
	GEP=0;
	for i in range(0,(IHEIGHT-h),h):
		for j in range(0,(IWIDTH-w),w):
			if(i+h>=IHEIGHT or w+j>=IWIDTH): print(hi,wj);break;

			eper=0; para=-1;
			for hi in range(i,(i+h)):
				for wj in range(j,(j+w)):
					if ( (wj>=ipsx and wj<ipex) and (hi>=ipsy and hi<ipey) ): continue;
					oavg = (int(adoimg[hi,wj,0]) + int(adoimg[hi,wj,1]) + int(adoimg[hi,wj,2]))//3;
					navg = (int(adnimg[hi,wj,0]) + int(adnimg[hi,wj,1]) + int(adnimg[hi,wj,2]))//3;
					# if (adoimg[hi,wj,0] == OBG): adoimg[hi,wj]=[0,255,0];
					# if (adnimg[hi,wj,0] == NBG): adnimg[hi,wj]=[0,255,0];
					# lpara = abs(int(adoimg[hi,wj,0]) - int(adnimg[hi,wj,0]))
					lpara = abs(int(oavg) - int(navg))
					if ( lpara!=0 and lpara!=para ) :
						eper+=1; para=lpara if (para==-1) else -1;
			GEP+=eper
			if (eper/(h*w)>(50/100)):
				match=False
				for hi in range(i,(i+h)):
					for wj in range(j,(j+w)):
							adoimg[hi,wj]=[255,0,0];adnimg[hi,wj]=[255,0,0];
	print(5,datetime.now())
	print(match,cf,"DIFFERENT "+str( math.trunc((GEP*10000)/(IWIDTH*IHEIGHT))/100 )+"%")

	simg = Image.fromarray(adoimg)
	simg.save('io.jpg')
	# simg.save(cf+"_OUT"+ioim)
	simg = Image.fromarray(adnimg)
	simg.save('in.jpg')
	# simg.save(cf+"_OUT"+inim)

	# plt.imshow(adoimg)
	# plt.show()
	# plt.imshow(adnimg)
	# plt.show()
	return match

def get_data(cf, btn, w=0, h=0, ipsx=0, ipsy=0, ipex=0, ipey=0) :
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
			compareIMG(cf,diofs+"\\"+imofs[j],dinfs+"\\"+imnfs[j], 20, 2,ipex=300,ipey=300)
			print('e',datetime.now())
			break;
		break;

	# btn.SetLabel("DONE!")
	return "OK"

COMPARE_FOLD = u".\\CompareFolder"
print(get_data(COMPARE_FOLD,'btn'))