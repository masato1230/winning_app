# Generated by Django 3.1.2 on 2020-11-03 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winning_app', '0002_auto_20201103_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='goods',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='replies',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]