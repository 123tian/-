


				//var oUl=document.getElementById('nav');
				var oUl=document.querySelector('nav');
				var oLi=oUl.getElementsByTagName("li");
				console.log(oLi);
				var oList=document.querySelector('list');
				var oDiv=oList.querySelector('div');
				console.log(oDiv);

				for (var  i=0;i<oLi.length;i++) {
					oLi[i].index=i;

					oLi[i].onclick=function(){
						for (var j=0;j<oLi.length;j++) {
							oLi[j].className='';
							oDiv[j].style.display="none";
						}
						this.className='click';
						oDiv[this.index].style.display='block';

					}
				}