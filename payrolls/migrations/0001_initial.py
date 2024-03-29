# Generated by Django 5.0.1 on 2024-03-12 10:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemandeSFT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_enfant', models.CharField(max_length=255)),
                ('date_naissance_enfant', models.DateField()),
                ('date_demande', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('En attente', 'En attente'), ('Acceptée', 'Acceptée'), ('Refusée', 'Refusée')], default='En attente', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Paie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre_paie', models.CharField(max_length=255)),
                ('date_remboursement', models.DateTimeField(auto_now_add=True)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paies', to='employees.agent')),
            ],
        ),
        migrations.CreateModel(
            name='Indemnite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre_indemnite', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('montant', models.FloatField()),
                ('paie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='indemnites', to='payrolls.paie')),
            ],
        ),
        migrations.CreateModel(
            name='Cotisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_cotisation', models.CharField(choices=[('CSG', 'CSG'), ('CRDS', 'CRDS'), ('CSA', 'CSA'), ('Cotisation Assurance maladie', 'Cotisation Assurance maladie'), ('Cotisation chomage', 'Cotisation chomage'), ('Cotisation retraite', 'Cotisation retraite')], default='CSG', max_length=255)),
                ('taux', models.FloatField()),
                ('paies', models.ManyToManyField(blank=True, null=True, related_name='cotisations', to='payrolls.paie')),
            ],
        ),
        migrations.CreateModel(
            name='Prime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre_prime', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('montant', models.FloatField()),
                ('paies', models.ManyToManyField(blank=True, null=True, related_name='primes', to='payrolls.paie')),
            ],
        ),
    ]
