# Generated by Django 2.1.3 on 2018-12-13 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20181213_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(default=-8843, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default=-8843, max_length=20),
            preserve_default=False,
        ),
    ]