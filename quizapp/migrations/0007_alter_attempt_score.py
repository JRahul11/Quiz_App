# Generated by Django 3.2.5 on 2021-08-02 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0006_alter_attempt_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attempt',
            name='score',
            field=models.PositiveIntegerField(null=True),
        ),
    ]