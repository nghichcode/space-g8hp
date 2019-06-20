import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def compareIMG(ioim ,inim, w=0, h=0, ipsx=0, ipsy=0, ipex=0, ipey=0) :
	try:
		doimg = Image.open(ioim)
		dnimg = Image.open(inim)
	except IOError:
		print("Can not open")
		return
	match=True

	adoimg = np.array(doimg)
	adnimg = np.array(dnimg)
	IHEIGHT=len(adoimg)
	IWIDTH=len(adoimg[0])
	print(IWIDTH,IHEIGHT)
	ipex= ipex or IWIDTH
	ipey= ipey or IHEIGHT

	for i in range(IHEIGHT):
		for j in range(IWIDTH):
			avg = (int(adoimg[i,j,0]) + int(adoimg[i,j,1]) + int(adoimg[i,j,2]))//3;adoimg[i,j,0]=avg;adoimg[i,j,1]=avg;adoimg[i,j,2]=avg;
			avg = (int(adnimg[i,j,0]) + int(adnimg[i,j,1]) + int(adnimg[i,j,2]))//3;adnimg[i,j,0]=avg;adnimg[i,j,1]=avg;adnimg[i,j,2]=avg;

	plt.imshow(adoimg)
	plt.show()
	plt.imshow(adnimg)
	plt.show()

	# for (var i = 0; i < nimgData.data.length; i+=4 ) {
	# 	var avg=Math.floor( (oimgData.data[i]+oimgData.data[i+1]+oimgData.data[i+2])/3 );
	# 	oimgData.data[i]=avg;oimgData.data[i+1]=avg;oimgData.data[i+2]=avg;omColor.set(avg,omColor.get(avg)?omColor.get(avg)+1:1);
	# 	avg=Math.floor( (nimgData.data[i]+nimgData.data[i+1]+nimgData.data[i+2])/3 );
	# 	nimgData.data[i]=avg;nimgData.data[i+1]=avg;nimgData.data[i+2]=avg;nmColor.set(avg,nmColor.get(avg)?nmColor.get(avg)+1:1);
	# }


	print(ipex,ipey)

# function compareIMG(inim,ioim) {

#   function cpx(oimgData,nimgData) {
# 	  const ROW_BLOCK=40;////debug = 20
# 	  var omColor = new Map();
# 	  var nmColor = new Map();
# 	  // Black+White
#   	for (var i = 0; i < nimgData.data.length; i+=4 ) {
#   		var avg=Math.floor( (oimgData.data[i]+oimgData.data[i+1]+oimgData.data[i+2])/3 );
#   		// avg=(avg<196?0:255);
#   		oimgData.data[i]=avg;oimgData.data[i+1]=avg;oimgData.data[i+2]=avg;omColor.set(avg,omColor.get(avg)?omColor.get(avg)+1:1);
#   		avg=Math.floor( (nimgData.data[i]+nimgData.data[i+1]+nimgData.data[i+2])/3 );
#   		// avg=(avg<196?0:255);
#   		nimgData.data[i]=avg;nimgData.data[i+1]=avg;nimgData.data[i+2]=avg;nmColor.set(avg,nmColor.get(avg)?nmColor.get(avg)+1:1);
#   	}
#   	var OBG=0;var NBG=0;var MOBG=0;var MNBG=0;
#   	omColor.forEach(function(val,key) {if(val>MOBG){MOBG=val;OBG=key;}});
#   	nmColor.forEach(function(val,key) {if(val>MNBG){MNBG=val;NBG=key;}});
#   	// SET-BGCOLOR - BLUE
#   	for (var i = 0; i < nimgData.data.length; i+=4 ) {
#   		// if (oimgData.data[i]==OBG) {oimgData.data[i]=0;oimgData.data[i+1]=128;oimgData.data[i+2]=128;}
#   		// if (nimgData.data[i]==NBG) {nimgData.data[i]=0;nimgData.data[i+1]=128;nimgData.data[i+2]=128;}
#   	}
#   	// Remove Time - RED
#   	for (var i = 0; i < 4*40*1920; i+=4 ) {
#   		oimgData.data[i]=255;oimgData.data[i+1]=0;oimgData.data[i+2]=0;
#   		nimgData.data[i]=255;nimgData.data[i+1]=0;nimgData.data[i+2]=0;
#   	}
# 	  for (var i = 4*40*1920; i < nimgData.data.length; i+=(4*ROW_BLOCK) ) {// Different
# 	  	var eper=0; var para=0;
# 	  	for (var j=i; j<i+(4*ROW_BLOCK) ; j+=4) {
# 	  		if (nimgData.data[j] != oimgData.data[j] && (nimgData.data[j]-oimgData.data[j])!=para ){eper+=4;para=(nimgData.data[j]-oimgData.data[j]);}
# 	  	}
# 	  	if(eper/(ROW_BLOCK*4)>(50/100)) {// Draw error
# 	  		match=false;
# 	  		for (var j=i; j<i+(4*ROW_BLOCK) ; j+=4) {
# 	  			oimgData.data[j]=255;oimgData.data[j+1]=255;oimgData.data[j+2]=0;
# 	  			nimgData.data[j]=255;nimgData.data[j+1]=255;nimgData.data[j+2]=0;
# 	  		}
#   			// break;
# 	  	}
# 	  }
# 		ctxo.putImageData(oimgData, 0, 0);
# 		ctxn.putImageData(nimgData, 0, 0);
# 		if (!match) {console.warn("NOT MATCH",inim,ioim);}
# 		//else {console.log("MATCH",inim,ioim);}
#   }// ECPX
# }//compareIMG


def get_data(cf, w=0, h=0, ipsx=0, ipsy=0, ipex=0, ipey=0) :
	ncdir = []
	for r, d, f in os.walk(cf):
		ncdir=d; break;

	if (len(ncdir) != 2):
		return "Child Folders != 2 folders"

	dofs = cf+"\\"+ncdir[1]; dnfs = cf+"\\"+ncdir[0];

	infs=[]; iofs=[];
	for r, d, f in os.walk(dofs):
		iofs=d; break;
	for r, d, f in os.walk(dnfs):
		infs=d; break;
	if (len(iofs) != len(infs)):
		return "Folders To Compare is Different length"
	for i in range(len(iofs)):
		if (iofs[i]!=infs[i]):
			return "Folders To Compare are Different Name"
		diofs=dofs+"\\"+iofs[i];dinfs=dnfs+"\\"+infs[i];
		# print(diofs,dinfs)
		imofs=[];imnfs=[]
		for r, d, f in os.walk(diofs):
			imofs=f; break;
		for r, d, f in os.walk(dinfs):
			imnfs=f; break;
		imofs=sorted(imofs); imnfs=sorted(imnfs);
		
		if (len(imofs)!=len(imnfs)):
			return "Images in folder are Different length"
		for i in range(len(imofs)):
			compareIMG(diofs+"\\"+imofs[i],dinfs+"\\"+imnfs[i])
			return "B1"

	return "OK"

COMPARE_FOLD = u".\\CompareFolder"
print(get_data(COMPARE_FOLD, 30, 20))