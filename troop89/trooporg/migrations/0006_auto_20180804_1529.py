# Generated by Django 2.1 on 2018-08-04 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trooporg', '0005_auto_20180804_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='nickname',
            field=models.CharField(blank=True, max_length=32, null=True, unique=True),
        ),
    ]
