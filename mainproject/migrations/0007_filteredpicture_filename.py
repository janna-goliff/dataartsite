# Generated by Django 3.1.7 on 2021-04-27 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainproject', '0006_auto_20210427_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='filteredpicture',
            name='filename',
            field=models.CharField(default='filler', max_length=50, unique=True),
        ),
    ]
