# Generated by Django 3.1.7 on 2021-04-27 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainproject', '0005_picture_assoc_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='assoc_url',
            field=models.CharField(default='filler', max_length=50),
        ),
    ]
