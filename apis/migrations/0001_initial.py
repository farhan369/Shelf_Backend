# Generated by Django 3.2.3 on 2021-06-19 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(default=None, max_length=30, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('roll_no', models.CharField(max_length=20)),
                ('semester', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], max_length=10)),
                ('batch', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G')], max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('datetime', models.DateTimeField()),
                ('location', models.CharField(max_length=30)),
                ('max_participants', models.IntegerField()),
                ('short_description', models.CharField(max_length=150)),
                ('long_description', models.TextField()),
                ('poster', models.ImageField(upload_to='uploads/events')),
                ('reg_open_date', models.DateTimeField()),
                ('reg_close_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='EventRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.BooleanField(default=False)),
                ('photosubmission', models.ImageField(max_length=200, upload_to='pic')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'event')},
            },
        ),
        migrations.AddField(
            model_name='event',
            name='registrations',
            field=models.ManyToManyField(related_name='registered_events', through='apis.EventRegistration', to=settings.AUTH_USER_MODEL),
        ),
    ]
