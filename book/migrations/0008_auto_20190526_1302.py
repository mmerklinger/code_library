# Generated by Django 2.2.1 on 2019-05-26 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_auto_20190526_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='topic',
            field=models.CharField(max_length=50),
        ),
    ]
