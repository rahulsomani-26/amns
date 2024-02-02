from django.urls import path 
from .views import add, listd ,delete

urlpatterns = [
    path('add/',view=add,name='add'),
    path('list/',view=listd,name='list'),
    path('delete/<int:todo_id>',view=delete,name='delete'),
]