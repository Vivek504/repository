# Generated by Django 3.1.7 on 2021-03-20 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymentModule', '0011_auto_20210320_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket_details',
            name='arrival_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='ticket_details',
            name='departure_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='ticket_details',
            name='departure_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='ticket_details',
            name='travellers',
            field=models.IntegerField(),
        ),
    ]
