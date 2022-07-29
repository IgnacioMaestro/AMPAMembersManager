# Generated by Django 4.0.6 on 2022-07-26 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ampa_members_manager', '0058_rename_single_activities_in_activity_remittance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityremittance',
            name='payable_parts',
            field=models.ManyToManyField(to='ampa_members_manager.activitypayablepart', verbose_name='Activity Payable Parts'),
        ),
    ]