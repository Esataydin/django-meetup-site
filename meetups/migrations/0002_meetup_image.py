# Generated by Django 5.1.5 on 2025-01-24 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meetups", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="meetup",
            name="image",
            field=models.ImageField(default="test", upload_to="images"),
            preserve_default=False,
        ),
    ]
