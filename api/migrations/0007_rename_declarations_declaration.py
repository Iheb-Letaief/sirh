# Generated by Django 5.0.1 on 2024-02-27 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_contrat_prime_remove_paie_agents_paie_agent_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Declarations',
            new_name='Declaration',
        ),
    ]
