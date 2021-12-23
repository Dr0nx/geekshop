# Generated by Django 3.2.9 on 2021-12-19 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bdate',
            field=models.CharField(blank=True, max_length=8, verbose_name='дата рождения'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='langs',
            field=models.CharField(blank=True, default='RU', max_length=10, verbose_name='язык'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'М'), ('F', 'Ж')], max_length=1, verbose_name='пол'),
        ),
    ]
