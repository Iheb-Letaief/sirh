# Generated by Django 5.0.1 on 2024-03-05 15:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_naissance', models.DateField()),
                ('statut', models.CharField(max_length=255)),
                ('nationality', models.CharField(max_length=255)),
                ('cin', models.CharField(max_length=255)),
                ('date_embauche', models.DateField()),
                ('nb_enfants', models.IntegerField(default=0)),
                ('nb_heure', models.IntegerField(default=0)),
                ('taux_cotisation', models.IntegerField(default=0)),
                ('taux_impot', models.IntegerField(default=0)),
                ('salaire_horaire', models.FloatField(default=0)),
                ('conges_maladie', models.IntegerField(default=0)),
                ('conges_payes', models.IntegerField(default=0)),
                ('conges_bonifies', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('contrat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agents', to='contracts.contrat')),
            ],
        ),
        migrations.CreateModel(
            name='Poste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre_poste', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('droit_NBI', models.BooleanField(default=False)),
                ('droit_ZUS', models.BooleanField(default=False)),
                ('droit_IFSE', models.BooleanField(default=False)),
                ('droit_CIA', models.BooleanField(default=False)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='postes', to='employees.agent')),
            ],
        ),
    ]
