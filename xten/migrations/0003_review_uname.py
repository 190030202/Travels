# Generated by Django 2.2.20 on 2021-05-13 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xten', '0002_review_placename'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='uname',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
