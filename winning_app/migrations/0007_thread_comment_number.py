# Generated by Django 3.1.2 on 2020-11-05 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winning_app', '0006_auto_20201104_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='comment_number',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]