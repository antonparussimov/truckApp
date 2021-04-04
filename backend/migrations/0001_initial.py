# Generated by Django 2.2.8 on 2021-04-04 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TruckItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=256)),
                ('singleImage', models.ImageField(upload_to='uploads/trucks/singleImages')),
                ('multiImage', models.ImageField(upload_to='uploads/trucks/multiImages')),
            ],
        ),
    ]