# Generated by Django 2.2.4 on 2019-12-20 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='contactNo',
            field=models.IntegerField(default=False, unique=True),
        ),
    ]
