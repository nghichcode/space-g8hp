import re
import os
import numpy as np
import cv2
import imghdr
import pytesseract

pxSigma = 2

def compareIMG(outcf,outfo, cfo,ioim ,pcrt=10, ipsx=0, ipsy=0, ipex=0, ipey=0) :
	if (imghdr.what(cfo+"\\"+ioim)==None):
		return "Stat: Not IMG"
	# Load Image
	try:
		doimg = cv2.imread(cfo+"\\"+ioim)
	except IOError:
		print("Can not open")
		return "Stat: Can't open img"
	# Convert RGB to Black and white
	adoimg = np.trunc(np.average(doimg, axis=2)).astype(int)

	# Image height
	IHEIGHT=adoimg.shape[0]
	IWIDTH=adoimg.shape[1]
	#	Remove Different pixel
	if (ipey==-1): ipey=IHEIGHT
	if (ipex==-1): ipex=IWIDTH
	adoimg[ipsy:ipey,ipsx:ipex]=255
	# To txt
	tdo=pytesseract.image_to_string(adoimg)

	print(1, "tdo")
	print(tdo)
	fwpb= open(outfo+"\\"+ioim+".txt","w+")
	fwpb.write(tdo)
	fwpb.close()
	return "success"

def get_data(cfo,outcf, pcrt=10, ipsx=0, ipsy=0, ipex=0, ipey=0) :
	if ( (ipsx>ipex and ipex!=-1) or (ipsy>ipey and ipey!=-1) or (ipsx<0 or ipsy<0 or ipex<-1 or ipey<-1) ):
		yield "Input not valid"
		return "error"
	if (pcrt<0 or pcrt>100):
		yield "Accurate not valid"
		return "error"
	owcfo=os.walk(cfo)
	if (not os.path.exists(cfo) or not os.path.exists(outcf)):
		yield "Folder Not Exists"
		return "error"
	# Make dir
	try:
		os.makedirs(outcf+"\\COMPARE_OUT_A2\\TxtOut");
	except FileExistsError as fee:
		pass

	while (True):
		try:
			nocfo = next(owcfo);
			outfo = outcf+"\\COMPARE_OUT_A2\\TxtOut\\"+nocfo[0].replace(cfo,'')
			# New folder
			try:
				os.makedirs(outfo);
			except FileExistsError as fee:
				pass
			# Sort file
			imsfo=sorted(nocfo[2], key=lambda vr:[int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', vr) ] )
			for i in range(len(imsfo)):
				cpi = compareIMG(outcf,outfo, nocfo[0],imsfo[i], pcrt, ipsx,ipsy,ipex,ipey)
				if (cpi != "success" and cpi != "different"): yield cpi
				else : yield "Stat: "+str(i+1)+"/"+str(len(imsfo))+" of Infinity"
		except StopIteration as e:
			break;
	yield "Success!"
	return

# Unit Test
# NEW_FOLD = u"D:\\ReactJS\\public\\compare-image\\CPN\\SS1\\User Type Permission"
# OLD_FOLD = u"D:\\ReactJS\\public\\compare-image\\CPN\\SS2\\User Type Permission"

# NEW_FOLD = u"D:\\ReactJS\\public\\compare-image\\ON1"
# OLD_FOLD = u"D:\\ReactJS\\public\\compare-image\\ON2"

# NEW_FOLD = u"D:\\ReactJS\\public\\compare-image\\CPN\\SS1"
# OLD_FOLD = u"D:\\ReactJS\\public\\compare-image\\CPN\\SS2"

# NEW_FOLD = u"D:\\space-g8hp\\ToolsImageCompare_dev\\Z11"
# OLD_FOLD = u"D:\\space-g8hp\\ToolsImageCompare_dev\\Z12"
# from datetime import datetime
# print(datetime.now().timestamp())
# for rs in get_data("TRAIN",NEW_FOLD, OLD_FOLD, 0, 0,0,-1,40):
# 	# pass
# 	print(rs)
# print(datetime.now().timestamp())