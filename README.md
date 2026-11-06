# 📊 Analyse exploratoire et interprétation métier · Notebooks et données

# Brief · Crédit Azur
Entreprise et données fictives, conçues pour la formation.

# Les commanditaires
Marc Leroy, directeur des risques, et Inès Benali, responsable conformité. Crédit Azur propose du crédit à la consommation en agence, en ligne et via des courtiers.

# Le contexte
Le 1er mars 2024, un nouveau modèle de score (« score V2 ») a remplacé l'ancien pour décider de l'accord des crédits. Il pèse davantage l'ancienneté dans l'emploi et le type de contrat.
Depuis, la production a baissé et des associations de consommateurs interpellent la banque sur l'accès au crédit des jeunes actifs.
Le score d'octroi de crédit est un système d'IA à haut risque au sens du règlement européen sur l'IA : la conformité veut un état des lieux documenté.

# La demande
Comment évoluent les demandes, la production et le produit net bancaire (PNB) estimé ? Quelle saisonnalité, quel effet du score V2 ?
Quels types de crédit et quels canaux portent l'activité ?
Le score V2 a-t-il créé ou accentué des écarts entre groupes (âge, genre, région) ? Ces écarts s'expliquent-ils par des critères de risque ?
Que recommandez-vous, avec quels indicateurs de suivi, y compris d'inclusion financière ?
Les données · banque_credit_azur.csv
Une ligne = une demande de crédit, de janvier 2023 à décembre 2025.

# Colonne	Description
date_demande	Date de la demande
demande_id, client_id	Identifiants
genre, age, tranche_age, region	Profil du demandeur
canal	agence, web ou courtier
type_credit	auto, travaux, personnel, renouvelable
montant_demande, duree_mois	Montant demandé (€) et durée
revenu_mensuel	Revenu net mensuel déclaré (€)
taux_endettement	Charges mensuelles, crédit compris, divisées par le revenu
anciennete_emploi_ans, contrat	Ancienneté dans l'emploi et type de contrat
score_algo	Score du modèle en vigueur à la date de la demande (0 à 1)
credit_accorde	1 si le crédit a été accordé
montant_accorde	Montant accordé (0 si refus)
pnb_estime_eur	Produit net bancaire estimé sur la durée du crédit
rembourse_sans_incident	1 si aucun incident sur 12 mois ; vide si le crédit a été refusé
reference_population.csv donne la répartition de la population française adulte (approximation pédagogique inspirée de l'INSEE).
