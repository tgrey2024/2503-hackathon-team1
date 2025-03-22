# Generated by Django 5.1.7 on 2025-03-22 09:45

import cloudinary.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0002_alter_timeline_description_alter_timeline_event_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='description',
            field=models.TextField(help_text='Enter a description of the event'),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='event',
            field=models.CharField(help_text='Enter the name of the event', max_length=255),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, help_text='Upload an image related to the event', max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='year',
            field=models.IntegerField(default=2000, help_text='Enter the year (YYYY)'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Honour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('timeline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='honours', to='timeline.timeline')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='honours', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('timeline', 'user'), name='unique_timeline_user')],
            },
        ),
    ]
