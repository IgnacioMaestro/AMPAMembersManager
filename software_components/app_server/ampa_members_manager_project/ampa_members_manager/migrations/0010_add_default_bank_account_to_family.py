# Generated by Django 4.0.3 on 2022-03-28 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ampa_members_manager', '0009_add_bank_accounts_to_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='default_bank_account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ampa_members_manager.bankaccount'),
        ),
    ]
