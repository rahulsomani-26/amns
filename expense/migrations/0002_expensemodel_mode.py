# Generated by Django 5.0.1 on 2024-01-31 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expensemodel',
            name='mode',
            field=models.CharField(choices=[('P', 'paid'), ('U', 'Udhar')], default='P', max_length=1),
        ),
    ]
