from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import StudentRegistration
from .models import User

# Create your views here.

def add_show(request):
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pw = form.cleaned_data['password']
            registration = User(name=nm, email=em, password=pw )
            registration.save()
            form = StudentRegistration()
    else:
        form = StudentRegistration() #blank form
    student = User.objects.all()
    return render(request, 'enroll/AddandShow.html',{'form':form, 'student':student})


def delete(request, id):
    if request.method == "POST":
        delete_data = User.objects.get(pk=id)
        delete_data.delete()
    return HttpResponseRedirect('/')


def update_(request, id):
    if request.method == 'POST':
        get_data = User.objects.get(pk=id)  #gets the id of data
        show_and_updatedata = StudentRegistration(request.POST, instance=get_data)   #shows the data in the form
        if show_and_updatedata.is_valid():
            show_and_updatedata.save()
            return redirect('/')
    else:
        get_data = User.objects.get(pk=id)  #gets the id of data
        show_and_updatedata = StudentRegistration(instance=get_data)
    return render(request, 'enroll/update.html', {'form':show_and_updatedata})
