<canvas id="myCanvas_o" width="1920" height="971"></canvas>
<canvas id="myCanvas_n" width="1920" height="971"></canvas>

<script type="text/javascript">
	var G_IMGS = {old:'',new:''};var G_FOLDS={old:'',new:''};
	const dir = {old:'./compare-image/F_OLD/',new:'./compare-image/F_NEW/'};

	function compareIMG(inim,ioim) {
		var match=true;var nimgData;var oimgData;
	  var co = document.getElementById("myCanvas_o");var ctxo = co.getContext("2d");
	  var cn = document.getElementById("myCanvas_n");var ctxn = cn.getContext("2d");

		var oim=new Image(1920,971);
		oim.onload = function() {
			ctxo.drawImage(oim, 0, 0);oimgData = ctxo.getImageData(0, 0, co.width, co.height);
			oimgData && nimgData ?cpx(nimgData,oimgData):0;
		}
		oim.src=ioim;

		var nim=new Image(1920,971);
		nim.onload = function() {
			ctxn.drawImage(nim, 0, 0);nimgData = ctxn.getImageData(0, 0, cn.width, cn.height);
			oimgData && nimgData ?cpx(nimgData,oimgData):0;
		}
		nim.src=inim;

	  function cpx(oimgData,nimgData) {
		  const ROW_BLOCK=40;////debug = 20
		  var omColor = new Map();
		  var nmColor = new Map();
		  // Black+White
	  	for (var i = 0; i < nimgData.data.length; i+=4 ) {
	  		var avg=Math.floor( (oimgData.data[i]+oimgData.data[i+1]+oimgData.data[i+2])/3 );
	  		// avg=(avg<196?0:255);
	  		oimgData.data[i]=avg;oimgData.data[i+1]=avg;oimgData.data[i+2]=avg;omColor.set(avg,omColor.get(avg)?omColor.get(avg)+1:1);
	  		avg=Math.floor( (nimgData.data[i]+nimgData.data[i+1]+nimgData.data[i+2])/3 );
	  		// avg=(avg<196?0:255);
	  		nimgData.data[i]=avg;nimgData.data[i+1]=avg;nimgData.data[i+2]=avg;nmColor.set(avg,nmColor.get(avg)?nmColor.get(avg)+1:1);
	  	}
	  	var OBG=0;var NBG=0;var MOBG=0;var MNBG=0;
	  	omColor.forEach(function(val,key) {if(val>MOBG){MOBG=val;OBG=key;}});
	  	nmColor.forEach(function(val,key) {if(val>MNBG){MNBG=val;NBG=key;}});
	  	// SET-BGCOLOR - BLUE
	  	for (var i = 0; i < nimgData.data.length; i+=4 ) {
	  		// if (oimgData.data[i]==OBG) {oimgData.data[i]=0;oimgData.data[i+1]=128;oimgData.data[i+2]=128;}
	  		// if (nimgData.data[i]==NBG) {nimgData.data[i]=0;nimgData.data[i+1]=128;nimgData.data[i+2]=128;}
	  	}
	  	// Remove Time - RED
	  	for (var i = 0; i < 4*40*1920; i+=4 ) {
	  		oimgData.data[i]=255;oimgData.data[i+1]=0;oimgData.data[i+2]=0;
	  		nimgData.data[i]=255;nimgData.data[i+1]=0;nimgData.data[i+2]=0;
	  	}
		  for (var i = 4*40*1920; i < nimgData.data.length; i+=(4*ROW_BLOCK) ) {// Different
		  	var eper=0; var para=0;
		  	for (var j=i; j<i+(4*ROW_BLOCK) ; j+=4) {
		  		if (nimgData.data[j] != oimgData.data[j] && (nimgData.data[j]-oimgData.data[j])!=para ){eper+=4;para=(nimgData.data[j]-oimgData.data[j]);}
		  	}
		  	if(eper/(ROW_BLOCK*4)>(50/100)) {// Draw error
		  		match=false;
		  		for (var j=i; j<i+(4*ROW_BLOCK) ; j+=4) {
		  			oimgData.data[j]=255;oimgData.data[j+1]=255;oimgData.data[j+2]=0;
		  			nimgData.data[j]=255;nimgData.data[j+1]=255;nimgData.data[j+2]=0;
		  		}
	  			// break;
		  	}
		  }
			ctxo.putImageData(oimgData, 0, 0);
			ctxn.putImageData(nimgData, 0, 0);
			if (!match) {console.warn("NOT MATCH",inim,ioim);}
			//else {console.log("MATCH",inim,ioim);}
	  }// ECPX
	}//compareIMG

	async function get_data() {
		await $.getJSON('http://localhost:5555/ofolds',function(data){G_FOLDS.old=data;});
		await $.getJSON('http://localhost:5555/nfolds',function(data){G_FOLDS.new=data;});
		// for (var j=0; j<G_FOLDS.old.length; j++) {
		for (var j=0; j<1; j++) {
			await $.getJSON('http://localhost:5555/oimgs/'+G_FOLDS.old[j],function(data){G_IMGS.old=data;});
			await $.getJSON('http://localhost:5555/nimgs/'+G_FOLDS.new[j],function(data){G_IMGS.new=data;});
			console.log(G_IMGS);

			for (var i = 0; i < G_IMGS.old.length; i++) {
				if(i>15) {break;}//debug
				await compareIMG(dir.old+G_FOLDS.old[j]+'/'+G_IMGS.old[i],dir.new+G_FOLDS.new[j]+'/'+G_IMGS.new[i]);
			}
		}
	}//get_data
	get_data();
</script>
