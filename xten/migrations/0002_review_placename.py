# Generated by Django 2.2.20 on 2021-05-12 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xten', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='placename',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
