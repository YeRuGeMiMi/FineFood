
function waterfall(parent,box){
	//将main下的所有的class为box的元素取出
	var oParent=document.getElementById(parent);
	var oBoxs=getByClass(oParent,'box');
	//计算整个页面显示的页数
	var oBoxw = oBoxs[0].offsetWidth;
	//var clos = Math.floor(document.documentElement.clientWidth/oBoxw);
	//oParent.style.cssText="width:"+oBoxw*clos+"px;margin:0px auto;";
	var clos = Math.floor(oParent.offsetWidth/oBoxw);
	var hArr = [];  //存放列的高度
	for (var i = 0; i<oBoxs.length; i++) {
		if(i<clos){
			hArr.push(oBoxs[i].offsetHeight);
		}else{
			var minH = Math.min.apply(null,hArr);
			var index = getByArrayIndex(hArr,minH);
			oBoxs[i].style.position = "absolute";
			oBoxs[i].style.top = minH+'px';
			//oBoxs[i].style.left = oBoxw*index+'px';
			oBoxs[i].style.left = oBoxs[index].offsetLeft+'px';
			hArr[index]+=oBoxs[i].offsetHeight;
		}
		
	};
	
}

//取得一个节点的子节点中指定class的元素
function getByClass(parent,clsName){
	var boxArr=new Array();
	var oElements=parent.getElementsByTagName("*");
	for (var i = 0 ; i<oElements.length;i++) {
		if(oElements[i].className==clsName){
			boxArr.push(oElements[i]);
		}
	};
	return boxArr;
}

//取得数组指定元素的索引
function getByArrayIndex(arr,val){
	for(var i =0; i<arr.length;i++){
		if (arr[i]==val) {
			return i;
		};
	}
}

//检测拖动滚动条是否具备了加载数据块的条件
function checkScrollSlide(){
	var oParent = document.getElementById('main');
	var oBoxs = getByClass(oParent,'box');
	var lastBoxH = oBoxs[oBoxs.length-1].offsetTop;
	var scroTop = document.body.scrollTop || document.documentElement.scrollTop;
	var height = document.body.clientHeight || document.documentElement.clientHeight;
	var h = scroTop+height;
	return (lastBoxH < h)?true:false;
}

//获取XMLHttpRequest对象
function createXMLRequest(){
	var request = false;
	try {
                request = new ActivexObject("Msxml2.XMLHTTP");
            }
            catch (e1) {
                try {
                    request = new ActivexObject("Microsoft.XMLHTTP");
                }
                catch (e2) {
                    request = false;
                }
            }
            if (!request && typeof XMLHttpRequest != 'undefined') {
                request = new XMLHttpRequest();
            }

    return request;
}