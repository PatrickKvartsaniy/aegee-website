# Generated by Django 2.1 on 2018-08-27 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20180826_1711'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board_member',
            options={'verbose_name': 'Responsibility', 'verbose_name_plural': 'Board Members'},
        ),
        migrations.RenameField(
            model_name='board_member',
            old_name='name',
            new_name='name_in_english',
        ),
        migrations.AddField(
            model_name='board_member',
            name='name_in_ukrainian',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
