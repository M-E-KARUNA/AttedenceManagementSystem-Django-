from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from Stat.models import *
import sqlite3
import json;
st_data=[]
sub=[]
y={'18':'First','19':'Second','20':'Third','21':'Final'}
d={'5':'CSE'}
year=['First','Second','Third','Final']
branches=['CSE','ECE','EEE','MECH','FDT']
tables={'ThirdCSE':ThirdCSE,}
# Create your views here.
def login(r):
    global sub,st_data  
    if r.method=='POST':
        st_data1=ThirdCSE.objects.filter(roll=r.POST['roll']).values()
        try:
            st_data1=st_data1[0]
        except:
            return HttpResponse('not exist');   
        roll=r.POST['roll']
        name=st_data1['name']
        del st_data1['name']
        del st_data1['roll']

        del st_data1['id']
        sub=list(st_data1.keys())
        st_data2=OE.objects.filter(roll=r.POST['roll']).values()[0]
        sub.append(str(st_data2['oesubject'])) 
        st_data1[st_data2['oesubject']]=st_data2['oeat']
        st_data=list(st_data1.values())
        
        return render(r,'Stat/statistics.html',context={'name':name,'roll':roll,'sub':sub})
    elif r.META.get('HTTP_ACCEPT')=="*/*":
        st_dt=[[1 if not d[i-3:i].count('0') else (0 if not d[i-3:i].count('1') else d[i-3:i].count('1')/(3-d[i-3:i].count('-'))) for i in range(3,len(d)+1,3)] for d  in st_data]
        per=[float(str(x.count('1')/(len(x)-x.count('-'))*100)[:5]) for x in st_data]
        print(per)
        return JsonResponse({'datas':st_dt,'sub':sub,'per':per});
    return render(r,'Stat/login.html');

        
                




def branch(r):
    
    res=render(r,'Stat/branch.html',context={'branch':branches,'year':''})
    return res
def admin(r,dept): 
    if r.method=='POST':
        name=r.POST['adminName']
        password=r.POST['password']
        conn=sqlite3.connect('db.sqlite3')
        co=conn.cursor()
        ad=co.execute("select dept from AdminDetail where dept=? and name=? and password=?",(dept,name,password)).fetchall()
        print(ad)
       # ad=AdminDetail.objects.filter(name=admin,dept=dept)
        #name=ad[0].password
        '''try:
            print(ad)
            
        except:
            return render(r,'Stat/admin.html',context={'branch':dept})'''
        if len(ad)>0:
        #if password==name and ad[0].dept==dept:
            return render(r,'Stat/year.html',context={'branch':year,'stbranch':dept})        
    return render(r,'Stat/admin.html',context={'branch':dept})
    
def selectedYear(r,year,dept):
    try:
        table=tables[year+dept]
    except:
        return render(r,'404.html');
    st_datas=table.objects.all().values()
    sub=st_datas[0].copy()
    sub.pop('roll')
    sub.pop('name')
    sub.pop('id')
    oe=OE.objects.values_list('oesubject')
    oe=set(oe)
    soe=[]
    print(oe)   
    for x in oe:
        soe+=x
    soe.sort()
    sub=list(sub.keys())
    sub1=sub.copy()
    tp=tc=0
    subjects=[]
    st_data=[]
    sub=[(x,len(st_datas[0].get(x))) for x in sub]
    for st in  st_datas:
        for s in sub1:
            x=list(st[s]).count('1')
            y=len(st[s])
            subjects.append(x)
            tp+=x;tc+=y
        for s in soe:
            ob=OE.objects.filter(roll=st['roll']).values()
            if s==ob[0]['oesubject']:
                l=list(ob[0]['oeat'])
                le=l.count('1')
                subjects.append(le)
                tp+=le
                tc+=len(l) 
            
            else:
                subjects.append(0)
        
        for s in soe:
            #to display only caps letter;
            """x=''
            for k in s:
                if ord(k)<97:
                    x+=k"""

            sub.append((s,len(OE.objects.filter(id=1).values()[0]['oeat'])))
            
               
        st_data.append((st['roll'],st['name'],subjects,tp,tc,str(tp/tc*100)[:5]))
        subjects=[]
        tp=0
   
    
            
        
    return render(r,'Stat/attedence.html',context={'data':st_data,'sub':sub,'dept':dept,'year':year,'tc':tc});
    

def find(r):
    rono=r.GET['id']
    sub=r.GET['sub']
    per=float(r.GET['per'])

    t_at=0
    #y.get(rono[:2])+d.get(rono[-3])
    dt=tables['ThirdCSE'].objects.filter(roll=rono).values()[0]
    if sub in dt.keys():
        t_at=dt[sub]
    else:
        
        t_at=OE.objects.filter(roll=rono).values()[0]['oeat']
        
    t_pt=t_at.count('1')
    t_cs=len(t_at)-t_at.count('-')
    try:
        cl_to_attend=int(((t_cs*per)-(t_pt*100))/(100-per))
    except:
        cl_to_attend=0
    
    return JsonResponse({'cl':cl_to_attend}) 
    
def at_list(r):
    sub=r.GET['sub']
    tb=r.GET['tb']
    try:  
        rolls=[x[0] for x in tables[tb].objects.values_list('roll')]
        at=list(tables[tb].objects.values_list(sub))
        at=[x[0].count('1') for x in at]
    except:
        rolls=[x[0] for x in OE.objects.values_list('roll')]
        print('here',rolls);
        at=list(OE.objects.values_list('oeat'))
        at=[x[0].count('1') for x in at]

    return JsonResponse({'rolls':rolls,'at':at})
def updateData(r):
    import sqlite3
    dt=r.GET['data']
    table=r.GET['tb']
    sub=r.GET['subject'];
    con=sqlite3.connect('db.sqlite3')
    co=con.cursor()
    rolls=co.execute('select roll from Stat_thirdcse')
    if sub=='robotics':
        return HttpResponse('try different options');
    for x,y in enumerate(dt,1):
        
        co.execute('update Stat_'+table.lower()+' set '+sub+'='+sub+'||? where id=?',(y,x))
    con.commit();    
    return HttpResponse('success');
           
        
    
    
    
    
    
        


