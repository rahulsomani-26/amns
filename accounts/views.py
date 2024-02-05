from django.shortcuts import render,redirect
from .forms import RegistrationForm 
from django.http import HttpResponse
from django.core.mail import send_mail 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate 
from django.contrib import messages 
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives

# for groups and users 
from django.contrib.auth.models import Group
from django.contrib.auth.models import User 

# Create your views here.

# def register(request):
#     if request.method =='POST':
#         registration_form =  RegistrationForm(request.POST)
#         if registration_form.is_valid():

#             user = registration_form.save()
#             login(request,user)

#             subject = 'Welcome to MySite'
#             message = 'Thank You for registering'
#             from_email = 'r.somani.26@gmail.com'
#             recipient_list = [registration_form.cleaned_data['email']]
#             send_mail(subject,message,from_email,recipient_list)
#             messages.success(request,'Registration Successful. Welcome !')
#             return redirect('registration_success') # Redirects to succcess page 
#     else:
#         registration_form = RegistrationForm()

#     return render(request,'register.html',{'title':"Sending mails","form":registration_form})


def register(request):
    if request.method =='POST':
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            user = registration_form.save()
            login(request,user)

            # Send customized mails 
            subject = 'Welcome to {}'.format(__name__)
            html_message = render_to_string('registration_email.html')
            plain_message = strip_tags(html_message)
            from_email = 'r.somani.26@gmail.com'
            to_email = [registration_form.cleaned_data['email']]
            email = EmailMultiAlternatives(subject,plain_message,from_email,to_email)
            email.attach_alternative(html_message,'text/html')
            email.send()
            messages.success(request,'Registration Successful. Welcome to AMNS')
            return redirect('registration_success')
    else:
        registration_form = RegistrationForm()
    return render(request,'register.html',{'form':registration_form})




def registration_success(request):
    return HttpResponse("Mail Sent Successfully")


def init_roles(request):
    user = User.objects.get(username='amit')
    user.is_active=True
    user.is_staff=True
    user.is_superuser=True
    user.save()
    admin_group,created = Group.objects.get_or_create(name='Admins')
    print(admin_group in user.groups.all())
    user.groups.add(admin_group)
    user_group,created = Group.objects.get_or_create(name='Users')
    return render(request,'init_roles.html')



