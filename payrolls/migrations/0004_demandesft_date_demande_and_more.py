# Generated by Django 5.0.1 on 2024-03-12 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payrolls', '0003_demandesft'),
    ]

    operations = [
        migrations.AddField(
            model_name='demandesft',
            name='date_demande',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='demandesft',
            name='date_naissance_enfant',
            field=models.DateField(null=True),
        ),
    ]