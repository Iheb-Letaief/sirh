# Generated by Django 5.0.1 on 2024-02-29 14:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_declarations_declaration'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='conges_maladie',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='agent',
            name='conges_payes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='agent',
            name='salaire_horaire',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='agent',
            name='contrat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agents', to='api.contrat'),
        ),
    ]
