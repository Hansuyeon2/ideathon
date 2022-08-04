# Generated by Django 4.0.6 on 2022-08-03 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, null=True)),
                ('writer', models.CharField(max_length=200, null=True)),
                ('genre', models.CharField(max_length=200, null=True)),
                ('summary', models.CharField(max_length=200, null=True)),
                ('pub_date', models.DateTimeField()),
                ('date', models.CharField(max_length=200, null=True)),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='post/')),
            ],
        ),
    ]
