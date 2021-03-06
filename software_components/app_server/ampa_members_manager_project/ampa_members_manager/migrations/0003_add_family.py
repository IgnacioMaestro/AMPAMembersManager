# Generated by Django 4.0.3 on 2022-03-28 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ampa_members_manager', '0002_add_established_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_surname', models.TextField()),
                ('second_surname', models.TextField()),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AddConstraint(
            model_name='family',
            constraint=models.UniqueConstraint(fields=('first_surname', 'second_surname'), name='unique_surnames'),
        ),
    ]
