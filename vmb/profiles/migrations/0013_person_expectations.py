# Generated by Django 2.2.7 on 2020-01-01 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_auto_20191230_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='expectations',
            field=models.TextField(max_length=300, null=True),
        ),
    ]
