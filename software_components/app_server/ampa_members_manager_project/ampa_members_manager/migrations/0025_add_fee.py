# Generated by Django 4.0.3 on 2022-05-13 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ampa_members_manager', '0024_add_payment_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='academiccourse',
            name='fee',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
