# Generated by Django 2.1.3 on 2018-12-04 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20181202_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gift_name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('date_given', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='GiftSuggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_suggested', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='friend',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.CharField(default='dude', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(default='chilling', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='friend',
            name='last_name',
            field=models.CharField(default='amigo', max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='giftsuggestion',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gift_suggestions', to='api.Customer'),
        ),
        migrations.AddField(
            model_name='giftsuggestion',
            name='friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Friend'),
        ),
        migrations.AddField(
            model_name='giftsuggestion',
            name='gift',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Gift'),
        ),
        migrations.AddField(
            model_name='gift',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gifts', to='api.Customer'),
        ),
    ]
