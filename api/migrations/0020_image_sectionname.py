# Generated by Django 2.1.3 on 2018-12-20 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20181218_0701'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='sectionName',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
