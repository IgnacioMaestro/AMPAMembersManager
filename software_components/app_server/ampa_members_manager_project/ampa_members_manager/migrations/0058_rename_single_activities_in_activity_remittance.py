# Generated by Django 4.0.6 on 2022-07-26 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ampa_members_manager', '0057_rename_verbose_single_activity_in_activity_registration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activityremittance',
            old_name='single_activities',
            new_name='payable_parts',
        ),
    ]