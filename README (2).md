# 📊 Analyse exploratoire et interprétation métier · Notebooks et données

Projet de 2 jours (Mastère 2 Data & IA, bloc BC2, compétences C2.6 à C2.10). Les données sont fictives, générées pour la formation.

| Dossier | Pour qui | Contenu |
|---|---|---|
| `data/` | **Tous** | Trois secteurs (commerce, banque, hôtellerie), leur brief (`BRIEF_*.md`), la population de référence, et le jeu de démonstration du Fournil Moderne. |
| `exercices/` | **Élèves** | Les notebooks dirigés, valables pour les trois secteurs : on choisit son secteur dans la première cellule. |

Tout se fait dans **Google Colab** : la première cellule de chaque notebook télécharge `config_projet.py` en une seconde, et chaque fichier de données se télécharge ensuite au premier usage, un seul à la fois. Rien à installer sur les postes, pas besoin de connecter Google Drive.

## Déroulé

| Moment | Formateur (`demos/`) | Élèves (`exercices/`) |
|---|---|---|
| J1 · 9h00 | Brief et constitution des groupes | `00_installation` |
| J1 · 9h15 | | `01_exploration_autonome` (30 min, sans consignes) |
| J1 · 9h45 | `D01_demo_exploration` | `02_univarie_bivarie` (10h00) |
| J1 · 11h00 | `D02_demo_series` | `03_series_temporelles` (11h20) |
| J1 · 13h45 | `D03_demo_biais` | `04_biais_fairlearn` (14h15), livrable Git à 17h00 |
| J2 · 9h15 | `D04_demo_dashboard` | `05_dashboard_plotly` (9h45), livrable HTML à 12h30 |
| J2 · 13h30 | | `06_recommandations`, puis restitutions |

## Dans Colab
1. Ouvrez le notebook depuis Google Drive (double-clic › Google Colaboratory).
2. Exécutez la première cellule « ⚙️ À exécuter en premier » : quelques secondes.
3. Choisissez votre secteur dans la cellule suivante : seul le fichier de ce secteur est téléchargé.
4. Pour versionner : *Fichier › Enregistrer une copie dans GitHub*.

En local (JupyterLab), gardez `config_projet.py` à côté des notebooks et le dossier `data/` juste au-dessus : rien n'est téléchargé.
