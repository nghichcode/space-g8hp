import re
import os
import numpy as np
import cv2
import imghdr

pxSigma = 2

def compareIMG(outcf, cfo,cfn, ioim,inim, pcrt=10) :
	if (not ioim.endswith("csv") or not inim.endswith("csv")):
		return "Stat: Not IMG"
	# Load Image
	try:
		docsv = open(cfo+"\\"+ioim,"r").read().splitlines()
		dncsv = open(cfn+"\\"+inim,"r").read().splitlines()
	except IOError:
		print("Can not open")
		return "Stat: Can't open csv"

	socsv=set(docsv)
	sncsv=set(dncsv)
	if(len(socsv)!=len(sncsv)):
		fwpb= open(outcf+"_CSOUT_A1.csv","a+")
		fwpb.write("\n\""+ioim+"\",\""+inim+"\",")
		fwpb.write("\"Different\",")
		fwpb.close()
		return "Stat: Different length"

	sacsv=socsv.difference(sncsv)
	
	awpf = (len(sacsv)/len(socsv))*100

	if (awpf>pcrt):
		print(3, "{0:.6f}% Different".format(awpf) )

		fwpb= open(outcf+"_CSOUT_A1.csv","a+")
		fwpb.write("\n\""+ioim+"\",\""+inim+"\",")
		fwpb.write("\"{0:.6f}% Different\",".format(awpf) )
		fwpb.close()
		return "different"
	return "success"

def get_data(cfo,cfn, pcrt=10) :
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
	# Create CSV file
	fwpb=open(outcf+"_CSOUT_A1.csv","w+")
	fwpb.write("\"----ToolsCSVCompare----\",\n")
	fwpb.write("\n\" FOLDER 1 \",\" FOLDER 2 \",\" DIFFERENT \",")
	fwpb.close()

	while (True):
		try:
			nocfo = next(owcfo);
			nocfn = next(owcfn);
			# Sort file
			imsfo=sorted(nocfo[2], key=lambda vr:[int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', vr) ] )
			imsfn=sorted(nocfn[2], key=lambda vr:[int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', vr) ] )
			if(len(imsfo) == len(imsfn)):
				if(len(imsfo)!=0):
					fwpb=open(outcf+"_CSOUT_A1.csv","a+")
					fwpb.write("\n\""+nocfo[0]+"\",\""+nocfn[0]+"\",")
					fwpb.close()
				for i in range(len(imsfn)):
					cpi = compareIMG(outcf,nocfo[0],nocfn[0],imsfo[i],imsfn[i], pcrt)
					if (cpi != "success" and cpi != "different"): yield cpi
					else : yield "Stat: "+str(i+1)+"/"+str(len(imsfo))+" of Infinity"
			else: yield "Different Struct";return;
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

NEW_FOLD = u"D:\\space-g8hp\\NCIC_dev\\Z12"
OLD_FOLD = u"D:\\space-g8hp\\NCIC_dev\\Z11"
# from datetime import datetime
# print(datetime.now().timestamp())
for rs in get_data(NEW_FOLD, OLD_FOLD, 0):
	# pass
	print(rs)
# print(datetime.now().timestamp())