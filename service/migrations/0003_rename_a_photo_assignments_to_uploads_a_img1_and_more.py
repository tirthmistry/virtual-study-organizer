# Generated by Django 4.2.5 on 2023-09-28 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("service", "0002_remove_assignments_to_uploads_a_link"),
    ]

    operations = [
        migrations.RenameField(
            model_name="assignments_to_uploads",
            old_name="a_photo",
            new_name="a_img1",
        ),
        migrations.AddField(
            model_name="assignments_to_uploads",
            name="a_img2",
            field=models.ImageField(default="", upload_to="static/images"),
        ),
        migrations.AddField(
            model_name="assignments_to_uploads",
            name="a_img3",
            field=models.ImageField(default="", upload_to="static/images"),
        ),
        migrations.AddField(
            model_name="assignments_to_uploads",
            name="a_img4",
            field=models.ImageField(default="", upload_to="static/images"),
        ),
        migrations.AddField(
            model_name="assignments_to_uploads",
            name="a_img5",
            field=models.ImageField(default="", upload_to="static/images"),
        ),
    ]
