# Generated by Django 2.2.5 on 2021-03-04 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='flight_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('capacity', models.IntegerField()),
                ('economy_price', models.IntegerField()),
                ('business_price', models.IntegerField()),
                ('first_class_price', models.IntegerField()),
                ('departure_time', models.TimeField()),
                ('arrival_time', models.TimeField()),
                ('flight_no', models.CharField(max_length=10)),
                ('company', models.CharField(max_length=20)),
            ],
            options={
                'unique_together': {('flight_no', 'departure_time', 'date')},
            },
        ),
    ]
