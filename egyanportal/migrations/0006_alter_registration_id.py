# Generated by Django 5.1 on 2024-08-30 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egyanportal', '0005_enquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='id',
            field=models.IntegerField(auto_created=(1, 1), primary_key=True, serialize=False),
        ),
    ]
