# Generated by Django 4.0.4 on 2022-08-05 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
