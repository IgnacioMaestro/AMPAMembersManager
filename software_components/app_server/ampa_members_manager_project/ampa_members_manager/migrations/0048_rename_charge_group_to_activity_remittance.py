# Generated by Django 4.0.6 on 2022-07-20 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ampa_members_manager', '0047_change_verbose_in_remittance'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ChargeGroup',
            new_name='ActivityRemittance',
        ),
    ]
