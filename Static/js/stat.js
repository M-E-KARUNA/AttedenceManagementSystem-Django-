    var xhttp=new XMLHttpRequest()
    xhttp.onload=function()
    {

    
    data=JSON.parse(this.responseText);
    for(var s in data.sub){
    document.getElementById('res'+data.sub[s]).innerHTML=data.per[s];
}
    var dps=[];

    var charts=[];
    var l=data.datas[0].length
for(var i in data.datas){
    dps.push([])
for(var j=0;j<l;j++){
    dps[i].push({x:j+1,y:data.datas[i][j]*100})
}  
}
    CanvasJS.addColorSet('g',['green']);
    for (var s in data.sub)
    {

    charts.push(new CanvasJS.Chart(data.sub[s],
    {
    colorSet:'g',
    animationEnabled:true,
    interactivityEnabled:true,
    animationDuration:1000,
    title:{text:data.sub[s]},toolTip:{enabled:true},axisX:{title:'week',minimum:0.5,interval:1,maxmimum:2},axisY:{title:'percentage',minimum:0.5,interval:10,maximum:105},data:[{type:'line',dataPoints:dps[s]}]}))
    charts[s].render();
    }
    //var updateInterval=200;
    //var x1=0
    /*var update=function(){
    for (var i in dps){
    dps[i].push({x:x1+1,y:data.datas[i][x1]*100})
    charts[i].render();
    }
    x1++;
    }
var si=setInterval(update,updateInterval)
function stop(){
clearInterval(si)
}
setTimeout(stop,updateInterval*data.datas[0].length)*/
}

    xhttp.open('GET','/Stat/login/',true);
    xhttp.send()


function get(sub)
{
var xhttp=new XMLHttpRequest()
xhttp.onload=function(){
document.getElementById('res'+sub).innerHTML=JSON.parse(this.responseText).cl+' classes should be <br> attended continuously';
}
xhttp.open('GET','/Stat/find/?id='+document.getElementById('roll').innerHTML+'&sub='+sub+'&per='+document.getElementById('per'+sub).value,true)
xhttp.setRequestHeader('Contype-Type','application/json')
xhttp.send()
}