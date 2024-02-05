from django.core.management.base import BaseCommand
from random import randint
class Command(BaseCommand):
    help = 'My Custom Command'
    def handle(self,*args,**kwargs):
        otp = randint(1000,9999)
        self.stdout.write(self.style.SUCCESS(otp))
       

