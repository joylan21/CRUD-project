from django.shortcuts import render,redirect
from .form import userform
from .models import user
from django.contrib import messages

# Create your views here.
def AddandShow(request):
    form=userform()
    if request.method=='POST':
        form=userform(request.POST)
        if form.is_valid():
            nm=form.cleaned_data['name']
            em=form.cleaned_data['email']
            ps=form.cleaned_data['password']

            if user.objects.filter(email=em):
                messages.error(request, 'Email already exists!')
                return redirect('AndandShow')

            if user.objects.filter(name=nm):
                messages.error(request, 'Username already exists')
                return redirect('AndandShow')

            reg=user(name=nm,email=em,password=ps)
            reg.save()
            return redirect('AndandShow')
    data=user.objects.all()
    print(data)
    context={'form':form,'data':data}
    return render(request, 'home/index.html',context)