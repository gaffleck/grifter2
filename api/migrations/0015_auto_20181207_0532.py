# Generated by Django 2.1.3 on 2018-12-07 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20181206_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('year', models.IntegerField(blank=True)),
                ('equipment_type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('image', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='friend',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='giftrecord',
            name='friend',
        ),
        migrations.RemoveField(
            model_name='giftsuggestion',
            name='friend',
        ),
        migrations.RemoveField(
            model_name='specialdate',
            name='friend',
        ),
        migrations.RenameModel(
            old_name='Customer',
            new_name='User',
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='api.User'),
        ),
        migrations.AddField(
            model_name='giftrecord',
            name='contact',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='gift_history', to='api.Contact'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='giftsuggestion',
            name='contact',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Contact'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialdate',
            name='contact',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='special_dates', to='api.Contact'),
            preserve_default=False,
        ),
    ]