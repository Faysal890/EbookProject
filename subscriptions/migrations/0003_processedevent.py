# Generated by Django 5.0.6 on 2024-11-20 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_subscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessedEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.CharField(max_length=255, unique=True)),
                ('processed_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
