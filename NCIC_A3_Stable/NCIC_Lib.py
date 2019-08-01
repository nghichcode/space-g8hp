import re
import os
import numpy as np
import cv2
import imghdr

pxSigma = 2

def compareIMG(outcf, cfo,cfn, ioim,inim, pcrt=10, ipsx=0, ipsy=0, ipex=0, ipey=0) :
	if (imghdr.what(cfo+"\\"+ioim)==None or imghdr.what(cfn+"\\"+inim)==None):
		print(ioim,inim)
		return "Stat: Not IMG"
	# Load Image
	try:
		doimg = cv2.imread(cfo+"\\"+ioim)
		dnimg = cv2.imread(cfn+"\\"+inim)
	except IOError:
		print("Can not open")
		return "Stat: Can't open img"
	# Convert RGB to Black and white
	adoimg = np.trunc(np.average(doimg, axis=2)).astype(int)
	adnimg = np.trunc(np.average(dnimg, axis=2)).astype(int)
	# IF image are different size : return
	if (len(adoimg)!=len(adnimg) or len(adoimg[0])!=len(adnimg[0]) ):
		fwpb= open(outcf+"_OUT_A3.csv","a+")
		fwpb.write("\n\""+ioim+"\",\""+inim+"\",")
		fwpb.write("Different Size,")
		fwpb.close()
		return "Stat: Error image size"
	# Image height
	IHEIGHT=adoimg.shape[0]
	IWIDTH=adoimg.shape[1]
	#	Remove Different pixel
	if (ipey==-1): ipey=IHEIGHT
	if (ipex==-1): ipex=IWIDTH
	adoimg[ipsy:ipey,ipsx:ipex]=255
	adnimg[ipsy:ipey,ipsx:ipex]=255

	# Remove Space
	bwavgo=np.average(adoimg,axis=1)
	bwtruo=np.trunc(bwavgo).astype(int)
	# mxo=np.argmax(np.bincount(bwtruo))
	shagwa=np.argwhere(bwtruo==bwavgo).reshape(-1)
	adoimg=np.delete(adoimg,shagwa,0)
	bwavgo=np.delete(bwavgo,shagwa)

	bwavgn=np.average(adnimg,axis=1)
	bwtrun=np.trunc(bwavgn).astype(int)
	# mxn=np.argmax(np.bincount(bwtrun))
	shagwa=np.argwhere(bwtrun==bwavgn).reshape(-1)
	adnimg=np.delete(adnimg,shagwa,0)
	bwavgn=np.delete(bwavgn,shagwa)

	if (adoimg.shape[0]>adnimg.shape[0]):
		adoimg=np.delete(adoimg,np.arange(adnimg.shape[0],adoimg.shape[0]),0)
		bwavgo=np.delete(bwavgo,np.arange(bwavgn.shape[0],bwavgo.shape[0]),0)
	else :
		adnimg=np.delete(adnimg,np.arange(adoimg.shape[0],adnimg.shape[0]),0)
		bwavgn=np.delete(bwavgn,np.arange(bwavgo.shape[0],bwavgn.shape[0]),0)
	# print(adoimg.shape,adnimg.shape,adoimg.shape[0],adoimg.shape[1],adnimg.shape[0],adnimg.shape[1])

	# A3
	i=0
	while ( i<len(bwavgo) ) :
		j=0
		while ( j<len(bwavgn) and i<len(bwavgo) ) :
			if( bwavgo[i] == bwavgn[j] ) :
				adoimg=np.delete(adoimg,i,0)
				bwavgo=np.delete(bwavgo,i,0)
				adnimg=np.delete(adnimg,j,0)
				bwavgn=np.delete(bwavgn,j,0)
				i-=1
				break
			j+=1
		i+=1

	# If different color > pxSigma : different = true(1); else = false(0)
	aasf = np.absolute(np.subtract( adoimg,adnimg ))
	abwf = np.where( aasf>pxSigma ,1,0)
	assf = np.sum(abwf)
	print(assf,IWIDTH,IHEIGHT)
	awpf = (assf/(IWIDTH*IHEIGHT))*100

	if (awpf>pcrt):
		print(3, "{0:.6f}% Different".format(awpf) )
		# If different old image pixel = 3(black), new = 252 (white)
		# adoimg=np.where(abwf!=1,3,adoimg)
		# adnimg=np.where(abwf!=1,252,adnimg)

		cv2.imwrite(outcf+"_OUT_A3\\Old\\"+ioim,adoimg)
		cv2.imwrite(outcf+"_OUT_A3\\New\\"+inim,adnimg)

		fwpb= open(outcf+"_OUT_A3.csv","a+")
		fwpb.write("\n\""+ioim+"\",\""+inim+"\",")
		fwpb.write("\"{0:.6f}% Different\",".format(awpf) )
		fwpb.close()
	return "success"

def get_data(cfo,cfn, pcrt=10, ipsx=0, ipsy=0, ipex=0, ipey=0) :
	if ( (ipsx>ipex and ipex!=-1) or (ipsy>ipey and ipey!=-1) or (ipsx<0 or ipsy<0 or ipex<-1 or ipey<-1) ):
		yield "Input not valid"
		return "error"
	if (pcrt<0 or pcrt>100):
		yield "Accurate not valid"
		return "error"
	owcfo=os.walk(cfo)
	owcfn=os.walk(cfn)
	if (not os.path.exists(cfo) or not os.path.exists(cfn)):
		yield "Folder Not Exists"
		return "error"

	# Make dir
	outcf=cfo[:cfo.rfind("\\")]+"\\RESULT"
	try:
		os.makedirs(outcf+"_OUT_A3\\Old");os.makedirs(outcf+"_OUT_A3\\New");
	except FileExistsError as fee:
		pass

	# Create CSV file
	fwpb=open(outcf+"_OUT_A3.csv","w+")
	fwpb.write("\"----NCIC----\",\n")
	fwpb.write("\n\" FOLDER 1 \",\" FOLDER 2 \",\" DIFFERENT \",")
	fwpb.close()

	while (True):
		try:
			nocfo = next(owcfo)
			nocfn = next(owcfn)
			# Sort file
			imsfo=sorted(nocfo[2], key=lambda vr:[int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', vr) ] )
			imsfn=sorted(nocfn[2], key=lambda vr:[int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', vr) ] )
			if(len(imsfo) == len(imsfn)):
				fwpb=open(outcf+"_OUT_A3.csv","a+")
				fwpb.write("\n\""+nocfo[0]+"\",\""+nocfn[0]+"\",")
				fwpb.close()
				for i in range(len(imsfn)):
					cpi = compareIMG(outcf,nocfo[0],nocfn[0],imsfo[i],imsfn[i], pcrt, ipsx,ipsy,ipex,ipey)
					if (cpi != "success"): yield cpi
					else : yield "Stat: "+str(i+1)+"/"+str(len(imsfo))+" of Infinity"
			else: yield "Different Struct"+nocfo[0]; return;
		except StopIteration as e:
			break
	yield "Success!"
	return

# Unit Test
# NEW_FOLD = u"D:\\ReactJS\\public\\compare-image\\CPN\\SS1\\User Type Permission"
# OLD_FOLD = u"D:\\ReactJS\\public\\compare-image\\CPN\\SS2\\User Type Permission"

NEW_FOLD = u"D:\\ReactJS\\public\\compare-image\\CPN\\NFD\\cb"
OLD_FOLD = u"D:\\ReactJS\\public\\compare-image\\CPN\\NFD\\ca"

# NEW_FOLD = u"D:\\ReactJS\\public\\compare-image\\CPN\\SS2"
# OLD_FOLD = u"D:\\ReactJS\\public\\compare-image\\CPN\\SS1"

# NEW_FOLD = u"D:\\space-g8hp\\NCIC_dev\\Z11"
# OLD_FOLD = u"D:\\space-g8hp\\NCIC_dev\\Z12"
from datetime import datetime
print(datetime.now().timestamp())
for rs in get_data(NEW_FOLD, OLD_FOLD, 0, 0,0,-1,40):
	print(rs)
print(datetime.now().timestamp())