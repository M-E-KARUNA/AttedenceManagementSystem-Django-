var by='';
var tb='';
var val=[];
var setp=false

var subject='';
function show(dy){
tb=dy;
by=document.getElementById('main').innerHTML;
subject=mylist.options[mylist.selectedIndex].text
var xhttp=new XMLHttpRequest()
xhttp.onload=function(){

var text="<div id='li'>";
;
text+="<h1 style='text-align:center;color:green;border:1px solid green;margin:10px;'>"+subject+"</h1>";
var res=JSON.parse(this.responseText);
for (var i in res.rolls){
val.push('0');
}
for(var i in res.rolls){
let r=res.rolls[i];
text+="<p><label id='c"+r+"'>"+r+"</label><label id="+r+">"+'('+res.at[i]+')'+"</label>"+"<button value="+r+" id='b1' style='--i:blue' onclick='add("+i+")'>PRESENT</button><button style='--i:red' value='a' id='b2' onclick='sub("+i+")'>ABSENT</button></p>";
}
text+="<button id='bu' onclick='sendData()'>save</button></div>"
document.getElementById('main').innerHTML=text;
}
xhttp.open('GET','/Stat/list_record/?tb='+dy+'&sub='+subject,true)
xhttp.send()
}
function sendData(){
var xhttp=new XMLHttpRequest()
xhttp.onload=function(){
var msg=JSON.parse(this.responseText).msg;
window.alert(msg);
}
xhttp.open('GET','/Stat/updateData/?data='+val+'&tb='+tb+'&subject='+subject,true)
xhttp.send()
}
function add(ind){
if(setp){return}
let x=document.getElementById('b1').value;
val[ind]='1';
let v=document.getElementById(x).innerHTML
v="("+eval(v.slice(1,-1)+'+1')+")";
document.getElementById(x).innerHTML=v;
document.getElementById('c'+x).style.color="green";
setp=true;
}
function sub(ind){
if ((setp)&&(val.length>=ind+1)){
let x=document.getElementById('b1').value;
let v=document.getElementById(x).innerHTML
v="("+eval(v.slice(1,-1)+'-1')+")";
document.getElementById(x).innerHTML=v;
document.getElementById('c'+x).style.color='red';
setp=false;
}
val[ind]='0'

}