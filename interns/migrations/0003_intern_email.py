# Generated by Django 5.1.7 on 2025-03-10 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("interns", "0002_alter_intern_options_alter_intern_contact_info_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="intern",
            name="email",
            field=models.EmailField(
                default=None, max_length=254, null=True, verbose_name="Почта"
            ),
        ),
    ]
