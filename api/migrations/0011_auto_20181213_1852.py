# Generated by Django 2.1.3 on 2018-12-14 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_twiliomessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='twiliomessage',
            name='ApiVersion',
            field=models.CharField(default=2019, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='twiliomessage',
            name='FromCity',
            field=models.CharField(default='vancouver', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='twiliomessage',
            name='FromCountry',
            field=models.CharField(default='canada', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='twiliomessage',
            name='FromState',
            field=models.CharField(default='bc', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='twiliomessage',
            name='FromZip',
            field=models.CharField(default=90210, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='twiliomessage',
            name='NumMedia',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='twiliomessage',
            name='NumSegments',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='twiliomessage',
            name='SmsMessageSid',
            field=models.CharField(default='asdfasdf324243432', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='twiliomessage',
            name='SmsSid',
            field=models.CharField(default='12312sfsda234', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='twiliomessage',
            name='SmsStatus',
            field=models.CharField(default='sent', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='twiliomessage',
            name='ToCity',
            field=models.CharField(default='vancouver', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='twiliomessage',
            name='ToCountry',
            field=models.CharField(default='canada', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='twiliomessage',
            name='ToState',
            field=models.CharField(default='bc', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='twiliomessage',
            name='ToZip',
            field=models.CharField(default=90210, max_length=20),
            preserve_default=False,
        ),
    ]
