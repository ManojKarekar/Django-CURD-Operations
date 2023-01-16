from django.shortcuts import render , HttpResponseRedirect

from .forms import StudentRegistration
from .models import User



def add_data(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm,email=em,password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    data = {"form":fm,"stu":stud}
    return render(request, "app1/addandshow.html",data)
  
    
    
# deleting data
def delete_data(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect("/")
    
    


def update_data(request , id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration( instance=pi)

    return render(request, "app1/updatestudent.html",{"form":fm})
    