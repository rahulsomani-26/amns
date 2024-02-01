from django.db import models

PAYMENT_CHOICES = {
    "P":"paid",
    "U":"Udhar",
}


class ExpenseModel(models.Model):
    price = models.IntegerField()
    item = models.CharField(max_length=100)
    mode = models.CharField(max_length=1,choices=PAYMENT_CHOICES,default='P')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.item}'



