from django.db.models import Sum

# constants
smic_mois = 1766.92
smic_heure = 11.65

smic_percentages = {
      (18, 1): 0.27,
      (18, 2): 0.39,
      (18, 3): 0.55,
      (19, 1): 0.27,
      (19, 2): 0.43,
      (19, 3): 0.61,
      (20, 1): 0.27,
      (20, 2): 0.51,
      (20, 3): 0.67,
      (21, 1): 0.53,
      (21, 2): 0.61,
      (21, 3): 0.78,
      (22, 1): 0.53,
      (22, 2): 0.61,
      (22, 3): 0.78,
      (23, 1): 0.53,
      (23, 2): 0.61,
      (23, 3): 0.78,
      (24, 1): 0.53,
      (24, 2): 0.61,
      (24, 3): 0.78,
      (25, 1): 0.53,
      (25, 2): 0.61,
      (25, 3): 0.78,
      (26, 1): 1.00,
      (26, 2): 1.00,
      (26, 3): 1.00,
  }


# Calculate base salary (weekly)
def calcul_salaire_base(agent):
    return agent.salaire_horaire * agent.nb_heure

# Calculate overtime pay (assuming standard workweek is 40 hours and overtime rate is 1.5x)
def calcul_salaire_heures_supp(agent, paie):
    heures_standards = agent.contrat.nb_heures
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


def get_pourcentage_smic(age, experience):
    return smic_percentages[(age, experience)]

#def calcul_salaire_apprenti(agent, paie):


# validators
def validate_paie(paie):
    if paie.salaire_net < 0:
        paie.salaire_base = 0
        paie.salaire_brut = 0
        paie.salaire_net = 0
    return paie

