# Generated by Django 4.2.5 on 2023-12-15 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TutorReg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=10)),
                ('mobileno', models.CharField(max_length=10)),
                ('fname', models.CharField(max_length=10)),
            ],
        ),
    ]
