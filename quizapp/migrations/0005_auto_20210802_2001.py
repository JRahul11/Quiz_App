# Generated by Django 3.2.5 on 2021-08-02 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0004_remove_quizzes_time_limit_mins'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='points',
            new_name='mark',
        ),
        migrations.RemoveField(
            model_name='attempt',
            name='attempter',
        ),
        migrations.AddField(
            model_name='attempt',
            name='score',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Attempter',
        ),
    ]
