# Generated by Django 2.1.7 on 2019-03-10 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carparking', '0004_auto_20190310_1757'),
    ]

    operations = [
        migrations.DeleteModel('parkingslots'),
        migrations.CreateModel(
            name='ParkingSlots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_id', models.IntegerField()),
                ('distance', models.IntegerField()),
                ('availibility_status', models.BooleanField(default=True)),
                ('car_registration_number', models.IntegerField(null=True,default=0)),
                ('car_color', models.CharField(max_length=200,blank=True)),
            ],
        ),
    ]

