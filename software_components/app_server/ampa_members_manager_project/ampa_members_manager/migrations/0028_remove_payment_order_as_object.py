# Generated by Django 4.0.3 on 2022-05-14 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ampa_members_manager', '0027_remove_familiar_activity_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityregistration',
            name='payment_order',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='PaymentOrder',
        ),
    ]
