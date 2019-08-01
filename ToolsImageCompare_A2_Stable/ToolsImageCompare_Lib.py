import re
import os
import numpy as np
import cv2
import imghdr

pxSigma = 2

def compareIMG(outcf,outfo,outfn, cfo,cfn, ioim,inim, pcrt=10, ipsx=0, ipsy=0, ipex=0, ipey=0) :
	if (imghdr.what(cfo+"\\"+ioim)==None or imghdr.what(cfn+"\\"+inim)==None):
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
		fwpb= open(outcf+"\\COMPARE_OUT_A2.csv","a+")
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

	# If different color > pxSigma : different = false(0); else = true(1)
	aasf = np.absolute(np.subtract( adoimg,adnimg ))
	abwf = np.where( aasf>pxSigma ,0,1)
	# # Sum similar pixel
	assf = np.sum(abwf)
	# print(assf)
	# # Percent different pixel
	awpf = (1-assf/(IWIDTH*IHEIGHT))*100

	if (awpf>pcrt):
		print(3, "{0:.6f}% Different".format(awpf) )
		# If different old image pixel = 3(black), new = 252 (white)
		adoimg=np.where(abwf!=1,3,adoimg)
		adnimg=np.where(abwf!=1,252,adnimg)

		cv2.imwrite(outfo+"\\"+ioim,adoimg)
		cv2.imwrite(outfn+"\\"+inim,adnimg)

		fwpb= open(outcf+"\\COMPARE_OUT_A2.csv","a+")
		fwpb.write("\n\""+ioim+"\",\""+inim+"\",")
		fwpb.write("\"{0:.6f}% \",".format(awpf) )
		fwpb.close()
		return "different"
	return "success"

def get_data(cfo,cfn,outcf, pcrt=10, ipsx=0, ipsy=0, ipex=0, ipey=0) :
	if ( (ipsx>ipex and ipex!=-1) or (ipsy>ipey and ipey!=-1) or (ipsx<0 or ipsy<0 or ipex<-1 or ipey<-1) ):
		yield "Input not valid"
		return "error"
	if (pcrt<0 or pcrt>100):
		yield "Accurate not valid"
		return "error"
	# Root, dir, file
	owcfo=os.walk(cfo)
	owcfn=os.walk(cfn)
	if (not os.path.exists(cfo) or not os.path.exists(cfn) or not os.path.exists(outcf)):
		yield "Folder Not Exists"
		return "error"
	# Make dir
	try:
		os.makedirs(outcf+"\\COMPARE_OUT_A2\\Old");os.makedirs(outcf+"\\COMPARE_OUT_A2\\New");
	except FileExistsError as fee:
		pass
	# Create CSV file
	fwpb=open(outcf+"\\COMPARE_OUT_A2.csv","w+")
	fwpb.write("\"----ToolsImageCompare----\",\n")
	fwpb.write("\n\" FOLDER 1 \",\" FOLDER 2 \",\" DIFFERENT \",")
	fwpb.close()

	while (True):
		try:
			nocfo = next(owcfo);
			nocfn = next(owcfn);
			outfo = outcf+"\\COMPARE_OUT_A2\\Old\\"+nocfo[0].replace(cfo,'')
			outfn = outcf+"\\COMPARE_OUT_A2\\New\\"+nocfn[0].replace(cfn,'')
			# New folder
			try:
				os.makedirs(outfo);os.makedirs(outfn);
			except FileExistsError as fee:
				pass
			# Sort file
			imsfo=sorted(nocfo[2], key=lambda vr:[int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', vr) ] )
			imsfn=sorted(nocfn[2], key=lambda vr:[int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', vr) ] )
			if(len(imsfo) == len(imsfn)):
				if(len(imsfo)!=0):
					fwpb=open(outcf+"\\COMPARE_OUT_A2.csv","a+")
					fwpb.write("\n\""+nocfo[0]+"\",\""+nocfn[0]+"\",")
					fwpb.close()
				for i in range(len(imsfn)):
					cpi = compareIMG(outcf,outfo,outfn ,nocfo[0],nocfn[0],imsfo[i],imsfn[i], pcrt, ipsx,ipsy,ipex,ipey)
					if (cpi != "success" and cpi != "different"): yield cpi
					else : yield "Stat: "+str(i+1)+"/"+str(len(imsfo))+" of Infinity"
			else:
				fwpb=open(outcf+"\\COMPARE_OUT_A2.csv","a+")
				fwpb.write("\n\""+nocfo[0]+"\",\""+nocfn[0]+"\",Error")
				fwpb.write("\n\""+str(len(imsfo))+"\",\""+str(len(imsfn))+"\",Files")
				fwpb.close()
				yield "Stat: Different Struct";
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