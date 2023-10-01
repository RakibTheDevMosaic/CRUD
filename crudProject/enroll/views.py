from django.shortcuts import render,HttpResponseRedirect
from .forms import StuReg
from.models import student
# Create your views here.
def add_show(req):
    if req.method=='POST':
        st=StuReg(req.POST)
        if st.is_valid():
            nm=st.cleaned_data['name']
            em=st.cleaned_data['email']
            pwd=st.cleaned_data['password']
            reg=student(name=nm,email=em,password=pwd)
            reg.save()
            st=StuReg()

    else:
        st=StuReg()
    studd=student.objects.all() 
    return render(req,'enroll/AddandShow.html',{'stu_details':st,'stu':studd})

# this function will update/edit
def up_data(req,id):
    if req.method=='POST':
        px=student.objects.get(pk=id)
        st=StuReg(req.POST,instance=px)
        if st.is_valid():
            st.save()
    else:
        px=student.objects.get(pk=id)
        st=StuReg(instance=px)        
    return render(req,'enroll/update.html',{'form':st})






# this function for delete data
def delete_data(req,id):
    if req.method=='POST':
        pi=student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')