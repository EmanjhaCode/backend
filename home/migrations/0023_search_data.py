# Generated by Django 2.2.4 on 2020-10-10 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_park_hotel_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.IntegerField()),
                ('loc', models.CharField(default='none', max_length=200)),
                ('user', models.CharField(default='none', max_length=200)),
            ],
        ),
    ]
