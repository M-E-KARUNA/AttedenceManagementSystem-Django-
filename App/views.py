from django.shortcuts import render,HttpResponse,redirect
from App.models import Student;

# Create your views here.
def fun(r):
    return render(r,'App/hello.html');
    return HttpResponse("<i>HELLO</i>");
def student_data(r):
    t=int(r.COOKIES.get('count',0))
    s=int(r.session.get('count',0))
    r.session['count']=s+1
    data=Student.objects.all()
    res= render(r,'App/st.html',context={'data':data,'cookie':t,'session':s})
    res.cookies['count']=t+1
    return res
def login(r):
    return render(r,'App/log.html')
def login_su(r):
    return render(r,'App/hello.html',context={'NAME':r.POST['name']})
def index(r):
    st=Student.objects.all()
    return render(r,'App/index.html',context={'data':st})
def insertdata(r):
    if r.method=='POST':
        Student(name=r.POST['name'],mark=r.POST['mark']).save()
        return redirect('index')
    return render(r,'App/insert.html')
def updatedata(r,id):
    if r.method=='POST':
        st=Student.objects.get(id=id)
        st.name=r.POST['name']
        st.mark=r.POST['mark']
        st.save()
        return redirect('index')
    st=Student.objects.get(id=id)
    return render(r,'App/update.html',context={'st':st})
def deletedata(r,id):
    Student.objects.get(id=id).delete()
    return redirect('index')


        

   
    