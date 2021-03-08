# Generated by Django 2.2.5 on 2021-03-07 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymentModule', '0006_paymenthistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='ticket_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('company', models.CharField(max_length=20)),
                ('flight_no', models.CharField(max_length=10)),
                ('departure_time', models.TimeField()),
                ('arrival_time', models.TimeField()),
                ('source', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('departure_date', models.DateField()),
                ('travellers', models.IntegerField()),
            ],
        ),
    ]