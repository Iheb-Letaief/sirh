from django.db.models import Sum


# Calculate base salary (monthly)
def calcul_salaire_base(agent):
    return agent.salaire_horaire * agent.nb_heure

# Calculate overtime pay (assuming standard workweek is 40 hours and overtime rate is 1.5x)
def calcul_salaire_heures_supp(agent, paie):
    heures_standards = 40
    taux_heures_supp = 1.5

    if agent.nb_heure <= heures_standards:
        return 0

    heures_supp = agent.nb_heure - heures_standards
    return heures_supp * taux_heures_supp * agent.salaire_horaire

# Calculate gross salary
def calcul_salaire_brut(agent, paie):
    total_primes = paie.primes.all().aggregate(total=Sum('montant'))['total'] or 0
    return calcul_salaire_base(agent) + calcul_salaire_heures_supp(agent, paie) + total_primes

# Calculate tax deduction
def calcul_deduction_impot(agent, paie):
    return calcul_salaire_brut(agent, paie) * (agent.taux_impot / 100)

# Calculate social contribution deduction
def calcul_deduction_cotisation_sociale(agent, paie):
    return calcul_salaire_brut(agent, paie) * (agent.taux_cotisation / 100)

# Calculate net salary(assuming only tax and contribution for now)
def calcul_salaire_net(agent, paie):
    salaire_brut = calcul_salaire_brut(agent, paie)
    deducion_impot = calcul_deduction_impot(agent, paie)
    cotisation_sociale = calcul_deduction_cotisation_sociale(agent, paie)
    return salaire_brut - deducion_impot - cotisation_sociale



