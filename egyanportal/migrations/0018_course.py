# Generated by Django 5.0.6 on 2024-09-05 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egyanportal', '0017_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('course', models.CharField(max_length=200)),
                ('addate', models.DateField()),
            ],
        ),
    ]
