import os
import numpy as np
#from PIL import Image
#import matplotlib.pyplot as plt
from datetime import datetime
import shutil
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
		return "Err CO"
	print(2,datetime.now())
	match=True
	# Black and white
	adoimg = np.trunc(np.average(doimg, axis=2)).astype(int)
	adnimg = np.trunc(np.average(dnimg, axis=2)).astype(int)
#	adoimg = cv2.cvtColor(doimg, cv2.COLOR_BGR2GRAY)
#	adnimg = cv2.cvtColor(dnimg, cv2.COLOR_BGR2GRAY)
	# TRUNC IMG
	if (len(adoimg)<len(adnimg) or len(adoimg[0])<len(adnimg[0]) ): return "Err L"
	IHEIGHT=len(adoimg)
	IWIDTH= len(adoimg[0])
	#	RemoveIP
	if (ipex==-1): ipex=IWIDTH
	if (ipey==-1): ipey=IHEIGHT
	adoimg[ipsy:ipey,ipsx:ipex]=0
	adnimg[ipsy:ipey,ipsx:ipex]=0
	# ALGO 1
	NIWIDTH=(IWIDTH-(IWIDTH % w)) if (w>1) else IWIDTH
	NIHEIGHT=IHEIGHT-(IHEIGHT % h) if (h>1) else IHEIGHT

	ndoimg = adoimg[0:NIHEIGHT,0:NIWIDTH]
	ndnimg = adnimg[0:NIHEIGHT,0:NIWIDTH]
	ndsimg = np.absolute(np.subtract(ndoimg,ndnimg))
	ndbimg = np.where(ndsimg>1,1,0)
	# PARALA
	if (w>1):
		ndsimg = np.reshape(ndsimg, (-1,w) )
		ndsimg = np.sum(ndsimg, axis=1)
		ndsimg = np.reshape(ndsimg, (-1,int(IWIDTH/w)) )

		ndbimg = np.reshape(ndbimg, (-1,w) )
		ndbimg = np.sum(ndbimg, axis=1)
		ndbimg = np.reshape(ndbimg, (-1,int(IWIDTH/w)) )
	if (h>1):
		ndsimg = ndsimg.T
		ndsimg = np.reshape(ndsimg, (-1,h) )
		ndsimg = np.sum(ndsimg, axis=1)
		ndsimg = np.reshape(ndsimg, (-1,int(IHEIGHT/h)) )

		ndbimg = ndbimg.T
		ndbimg = np.reshape(ndbimg, (-1,h) )
		ndbimg = np.sum(ndbimg, axis=1)
		ndbimg = np.reshape(ndbimg, (-1,int(IHEIGHT/h)) )
	# 1st : not para, 2nd : not diff in block
	ndsimg = np.where(np.trunc(ndsimg/(w*h))==ndsimg/(w*h),1,0 )
	ndbimg = np.where(ndbimg/(w*h)>0.5,1,0 )
	ndwimg = np.bitwise_or(ndsimg,ndbimg)
	ndffff = 100 * ( 1-np.average(ndwimg) )
	if (ndffff): match=False;
	print(3, "{0:.4f}% diff".format(ndffff) )
	# Diff ALGO 2
	aasf = np.absolute(np.subtract( adoimg,adnimg ))
#	absf = np.add( adoimg,adnimg )
	abwf = np.where(aasf>1 ,0,1)
#	abwg = np.where(absf/2 == np.trunc(absf/2) ,1,0 )
#	assf = np.bitwise_or(abwf,abwg)
	assf = np.sum(abwf)
	
	awpf = (1-assf/(IWIDTH*IHEIGHT))*100
	adoimg=np.where(abwf!=1,222,adoimg)
	adnimg=np.where(abwf!=1,222,adnimg)
	print(3, "{0:.4f}% diff".format(awpf) )
	print(3,datetime.now())

	cv2.imwrite(cf+"_OUT"+ioim,adoimg)
	cv2.imwrite(cf+"_OUT"+inim,adnimg)

	fwpa= open(cf+"_OUT_A1.txt","a+")
	fwpa.write("\n---- "+ioim+"::"+inim)
	fwpa.write("\n{0:.4f}% diff".format(ndffff) )
	fwpa.close()
	fwpb= open(cf+"_OUT_A2.txt","a+")
	fwpb.write("\n---- "+ioim+"::"+inim)
	fwpb.write("\n{0:.4f}% diff".format(awpf) )
	fwpb.close()
	return

	# simg = Image.fromarray(adoimg)
	# simg.save('io.jpg')
	# simg.save(cf+"_OUT"+ioim)
	# simg = Image.fromarray(adnimg)
	# simg.save('in.jpg')
	# simg.save(cf+"_OUT"+inim)

	# plt.imshow(adoimg)
	# plt.show()

def get_data(cf, w=0, h=0, ipsx=0, ipsy=0, ipex=0, ipey=0) :
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

	fwpa=open(cf+"_OUT_A1.txt","w+")
	fwpa.write("----"+str(datetime.now())+"----\n")
	fwpa.close()
	fwpb=open(cf+"_OUT_A2.txt","w+")
	fwpb.write("----"+str(datetime.now())+"----\n")
	fwpb.close()

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
		for r, d, f in os.walk(cf+diofs): imofs=f; break;
		for r, d, f in os.walk(cf+dinfs): imnfs=f; break;
		imofs=sorted(imofs); imnfs=sorted(imnfs);
		
		if (len(imofs) != len(imnfs)): return "Image items To Compare are Different Length"
		for j in range(len(imofs)):
			print('-------------------------------')
			print('s',datetime.now())
			compareIMG(cf,diofs+"\\"+imofs[j],dinfs+"\\"+imnfs[j], 30, 40,ipex=-1,ipey=30)
			yield str(j+1)+"/"+str(len(imofs))+" of "+str(i+1)+"/"+str(len(iofs))
			print('e',datetime.now())
			print('-----',diofs+"\\"+imofs[j],'-----')
#			break;
#		break;

	return "OK"

COMPARE_FOLD = u".\\CompareFolder"
for rs in get_data(COMPARE_FOLD):
	print(rs == None)