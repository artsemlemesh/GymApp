# Generated by Django 5.0.6 on 2024-06-10 04:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("schedule", "0002_classes_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="instructor",
            name="user_image",
            field=models.ImageField(blank=True, upload_to="image"),
        ),
    ]
