# Generated by Django 4.1.3 on 2022-11-05 07:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0003_review"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("name", models.CharField(max_length=200)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="review",
            name="value",
            field=models.CharField(
                choices=[("up", "up"), ("down", "down")], max_length=50
            ),
        ),
    ]