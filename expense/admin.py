from django.contrib import admin
from django.http import HttpResponse
from .models import ExpenseModel

@admin.action(description="if Paid Click to Change the Status")
def show(modeladmin,request,queryset):
    queryset.update(mode='P')

@admin.action(description="Just a test ")
def test(modeladmin,request,queryset):
    return HttpResponse(ExpenseModel.objects.all())

class ExpsenseAdmin(admin.ModelAdmin):
    search_fields = ['mode']
    list_display = ['item','price','mode']
    actions=[show,test]

admin.site.register(ExpenseModel,ExpsenseAdmin)
