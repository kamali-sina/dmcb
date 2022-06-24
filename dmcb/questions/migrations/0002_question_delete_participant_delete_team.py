# Generated by Django 4.0.5 on 2022-06-24 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "question_id",
                    models.CharField(
                        max_length=30, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("question_text", models.CharField(blank=True, max_length=200)),
                (
                    "difficulty",
                    models.CharField(
                        choices=[("E", "Easy"), ("M", "Medium"), ("H", "Hard")],
                        max_length=2,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Participant",
        ),
        migrations.DeleteModel(
            name="Team",
        ),
    ]