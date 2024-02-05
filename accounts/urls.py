
from django.urls import path,include
from .views import register, registration_success,init_roles

urlpatterns = [
    path('register/',view=register,name='register'),
    path('success/',view=registration_success,name='registration_success'),
    path('role/',view=init_roles,name='init_roles')
]
