# Generated by Django 5.2.3 on 2025-06-21 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_courses_image_alter_courses_lessons_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='courses',
            name='lessons_count',
            field=models.IntegerField(),
        ),
    ]
