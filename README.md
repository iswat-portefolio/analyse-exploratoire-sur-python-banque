# Crédit Azur — Analyse de l’activité et de l’accès au crédit

Projet d’analyse exploratoire réalisé en équipe avec Python,
à partir de données bancaires fictives couvrant janvier 2023
à décembre 2025.

L’objectif : comprendre la baisse de l’activité et les différences
d’accès au crédit observées autour du déploiement d’un nouveau score.

## Le contexte

En mars 2024, Crédit Azur déploie un score d’octroi de crédit
qui donne davantage de poids au contrat de travail et à
l’ancienneté professionnelle.

La banque constate une baisse de sa production. Des associations
questionnent également l’accès au crédit des jeunes actifs.

Notre étude vise à éclairer les décisions de la direction
des risques et de la conformité.

## Les questions étudiées

- Comment évoluent les demandes, les crédits accordés et le PNB estimé ?
- Quels produits portent l’activité ?
- Quels écarts d’accord observe-t-on selon l’âge, le genre et la région ?
- Comment ces écarts évoluent-ils après le déploiement du score V2 ?
- Quelles actions et quels indicateurs de suivi proposer ?

## Les données

Une ligne correspond à une demande de crédit.

- Période : janvier 2023 à décembre 2025.
- Volume initial : 20 477 demandes.
- Volume après nettoyage : 20 384 demandes.
- Produits : crédit personnel, auto, travaux et renouvelable.
- Canaux : agence, web et courtier.

Les données sont fictives et ont été fournies dans le cadre
d’une formation. Elles ne décrivent pas une banque réelle.

## Notre démarche

1. Contrôler les données : doublons, valeurs manquantes,
   types et valeurs incohérentes.
2. Décrire les distributions et comparer les types de crédit.
3. Étudier les tendances, la saisonnalité et les ruptures.
4. Mesurer la représentativité et les différences de taux d’accord.
5. Construire un dashboard interactif et proposer des actions.

Les analyses mobilisent notamment la corrélation de Spearman,
les tests de Kruskal-Wallis et du khi², la décomposition
saisonnière et les métriques de parité.

## Principaux résultats

| Indicateur | Résultat |
|---|---:|
| Demandes après nettoyage | 20 384 |
| Taux d’accord global sur 2023–2025 | 64,0 % |
| Part auto et travaux dans le PNB estimé sur 2023–2025 | 83,9 % |
| Évolution du PNB estimé des demandes de 2025 par rapport à 2024 | −5,0 % |
| Taux d’accord des 18–24 ans avant V2 | 36,1 % |
| Taux d’accord des 18–24 ans après V2 | 7,7 % |

La baisse des accords chez les jeunes justifie une analyse
approfondie des critères du score. Elle ne démontre pas,
à elle seule, une discrimination ni un effet causal de V2.

## Consulter le projet

| Étape | Notebook |
|---|---|
| Exploration | [01 — Exploration](01_yasmine_iswat_eba.ipynb) |
| Distributions et comparaisons | [02 — Analyse univariée et bivariée](02_yasmine_eba_iswat.ipynb) |
| Tendances et saisonnalité | [03 — Séries temporelles](03_yasmine_eba_iswat.ipynb) |
| Représentativité et disparités | [04 — Analyse des biais](04_yasmine_eba_iswat.ipynb) |
| Visualisation interactive | [05 — Dashboard Plotly](Copie_de_05_dashboard_plotly.ipynb) |
| Actions proposées | [06 — Recommandations](06_recommandations.ipynb) |

### Dashboard

Le [dashboard HTML](dashboard_banque_presentation.html) présente
l’activité, les produits, les écarts entre groupes et les recommandations.

Pour l’utiliser, télécharger le fichier puis l’ouvrir dans un navigateur.
Il fonctionne sans connexion. GitHub affiche son code, sans exécuter
directement les graphiques.

## Recommandations

- Analyser le rôle du contrat et de l’ancienneté professionnelle,
  en comparant des profils financiers similaires.
- Suivre conjointement l’activité et les incidents de remboursement.
- Organiser une revue régulière des écarts entre groupes,
  avec les effectifs et les limites d’interprétation.

## Limites

- Une comparaison avant/après ne démontre pas un lien de causalité.
- Les écarts entre groupes peuvent être partiellement expliqués
  par les profils financiers et professionnels.
- Les remboursements sont connus uniquement pour les crédits accordés :
  le calcul réalisé ne permet pas d’évaluer l’égalité des chances.
- La représentativité dépend de la population de référence retenue.
- Le PNB est estimé sur la durée des crédits et regroupé par mois
  de demande : ce n’est ni un encaissement mensuel ni un bénéfice net.

## Outils

Python · pandas · NumPy · SciPy · Matplotlib · Seaborn ·
statsmodels · Fairlearn · Plotly · Jupyter · VS Code

## Équipe et cadre pédagogique

Projet réalisé par Iswat Tairou, Yasmine et Eba dans le cadre
du cours « Analyse exploratoire et interprétation métier ».

Le brief, les données fictives, les modèles de notebooks et les
fonctions de configuration proviennent des supports pédagogiques
fournis par le formateur.

Ce dépôt présente notre travail d’analyse, d’interprétation
et de restitution à partir de ces supports.
