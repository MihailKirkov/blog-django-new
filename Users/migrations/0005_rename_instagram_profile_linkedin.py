# Generated by Django 4.2.6 on 2023-10-15 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_profile_facebook_profile_instagram_profile_website'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='instagram',
            new_name='linkedin',
        ),
    ]
