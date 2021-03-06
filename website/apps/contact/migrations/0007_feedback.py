# Generated by Django 2.1.1 on 2018-12-07 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_auto_20180827_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
