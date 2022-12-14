# Generated by Django 4.0.4 on 2022-08-05 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_comment_content_remove_comment_update_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='body',
        ),
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='update_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.post'),
        ),
    ]
