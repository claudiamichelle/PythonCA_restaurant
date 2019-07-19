# Generated by Django 2.2.2 on 2019-07-12 03:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='user',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='category',
            field=models.ForeignKey(blank=True, default=3, null=True, on_delete=django.db.models.deletion.CASCADE, to='reviews.category'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='review',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Restaurant'),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=10)),
                ('choice_comment', models.CharField(blank=True, max_length=200, null=True)),
                ('votes', models.IntegerField(default=0)),
                ('choice_user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Restaurant')),
            ],
        ),
    ]
