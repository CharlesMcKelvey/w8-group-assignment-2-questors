# Generated by Django 2.2.6 on 2019-11-02 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnswerQuest', '0004_auto_20191101_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='starred_answers',
            field=models.ManyToManyField(blank=True, related_name='Afans', to='AnswerQuest.Answer'),
        ),
    ]
