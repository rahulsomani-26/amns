from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User 

# Create your views here.

def register(request):
    print("Registering")
    if request.method == "POST":
        print(type(request.POST))
        print(request.POST.__dict__)
        name = request.POST.get("name")   
        password = request.POST.get("password",'NA')
        repeat = request.POST.get("repeat",'NA')
        email = request.POST.get("email",'NA')
        user = User.objects.create_user(username=name,email=email,password=password)
        user.save()

        print("__"*50)
        print(name,password,email,repeat)
        print("__"*50)
        return HttpResponse('<b> Hi {} your password is {}'.format(name,password))
    else:
        return render(request,'register.html')
    

