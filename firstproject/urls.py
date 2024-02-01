
from django.contrib import admin
from django.urls import path,include
from .views import startfn,index,getname

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', view=startfn,name='startfn'),
    path('',include('accounts.urls')),
    path('user/',include('accounts.urls')),
]
