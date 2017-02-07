# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('activity_type', models.CharField(max_length=1, choices=[('C', 'comment')])),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('post', models.IntegerField(null=True, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('notification_type', models.CharField(max_length=1, choices=[('C', 'Commented')])),
                ('is_read', models.BooleanField(default=False)),
                ('from_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='sender')),
                ('post', models.ForeignKey(null=True, to='posts.Post', blank=True)),
                ('to_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='receiver')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]
