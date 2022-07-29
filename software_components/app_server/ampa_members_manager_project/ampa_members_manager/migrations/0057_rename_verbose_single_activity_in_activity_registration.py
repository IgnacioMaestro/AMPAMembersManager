# Generated by Django 4.0.6 on 2022-07-26 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ampa_members_manager', '0056_rename_single_activity_in_activity_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityregistration',
            name='payable_part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ampa_members_manager.activitypayablepart', verbose_name='Activity Payable Part'),
        ),
    ]