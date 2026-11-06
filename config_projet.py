"""Configuration commune aux notebooks du projet : secteurs, accès aux données et outils.

Dans Colab, chaque fichier de données est téléchargé depuis Google Drive au premier usage
(un seul fichier, environ 2 Mo, une à deux secondes), puis gardé dans data/ pour la session.
"""
from pathlib import Path
import urllib.request
import pandas as pd

DATA = next((p for p in [Path("data"), Path("../data"), Path("../../data")]
             if (p / "reference_population.csv").exists()), Path("data"))

# Identifiants Google Drive des fichiers (partagés en lecture à toute personne disposant du lien).
# Pour mettre un fichier à jour sans changer son identifiant : Drive › clic droit › Gérer les versions.
FICHIERS_DRIVE = {
    "commerce_maison_lumen.csv": "1Rn1TTUrH_ZxHUgeUKPYuX1zd1kvy7ZQ4",
    "banque_credit_azur.csv": "1aArvpMkECAKBqCxmgHHOxbWRjtvGFdes",
    "hotellerie_les_escales.csv": "1amM1ruECR1V6-QDEagQ6j82x_l92dLgs",
    "demo_fournil_moderne.csv": "1AmKzGVFquNjIEH93LiRyieMH5Uk1xJ7c",
    "reference_population.csv": "1_OY2gskFlwo_6w6PHK0o1AXILV9446UL",
    "BRIEF_commerce.md": "1dqFbuL_LgyqCqZp7dpr17qDmCTaa5SkE",
    "BRIEF_banque.md": "1c5sxrfmk6UNdtnucWmGETVgfbImHhUrs",
    "BRIEF_hotellerie.md": "1Obdh__QtwLV2MuuA7P3dt1kcOWNnYelG",
}
URL_DRIVE = "https://drive.google.com/uc?export=download&id="


def fichier(nom):
    """Chemin local d'un fichier du cours, téléchargé depuis Drive s'il manque."""
    chemin = DATA / nom
    if chemin.exists():
        return chemin
    DATA.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(URL_DRIVE + FICHIERS_DRIVE[nom], timeout=60) as reponse:
        contenu = reponse.read()
    if contenu[:200].lstrip().lower().startswith((b"<!doctype html", b"<html")):
        raise PermissionError(f"{nom} n'est pas accessible : partagez-le dans Drive avec "
                              "« Tous les utilisateurs disposant du lien » (lecteur).")
    chemin.write_bytes(contenu)
    return chemin


CONFIG = {
    "commerce": dict(
        nom="Maison Lumen", fichier="commerce_maison_lumen.csv", dates=["date_commande"],
        date="date_commande", ca="montant_eur", ca_label="Chiffre d'affaires (€)",
        id="commande_id", decision="offre_personnalisee", decision_label="offre personnalisée envoyée",
        resultat="rachat_90j", sensibles=["tranche_age", "genre", "region"], segment="canal",
        evenement=("2024-04-15", "refonte du site et lancement de l'app"), atypiques=[]),
    "banque": dict(
        nom="Crédit Azur", fichier="banque_credit_azur.csv", dates=["date_demande"],
        date="date_demande", ca="pnb_estime_eur", ca_label="PNB estimé (€)",
        id="demande_id", decision="credit_accorde", decision_label="crédit accordé",
        resultat="rembourse_sans_incident", sensibles=["tranche_age", "genre", "region"], segment="type_credit",
        evenement=("2024-03-01", "déploiement du score V2"), atypiques=[]),
    "hotellerie": dict(
        nom="Les Escales", fichier="hotellerie_les_escales.csv", dates=["date_reservation", "date_arrivee"],
        date="date_arrivee", ca="ca_sejour_eur", ca_label="Chiffre d'affaires des séjours (€)",
        id="reservation_id", decision="surclassement_propose", decision_label="surclassement proposé",
        resultat="fidelise_12m", sensibles=["tranche_age", "genre", "pays_residence"], segment="canal",
        evenement=("2025-03-01", "nouveau moteur de réservation directe"),
        atypiques=["2024-07-01", "2024-08-01", "2024-09-01"]),
    "demo": dict(
        nom="Le Fournil Moderne", fichier="demo_fournil_moderne.csv", dates=["date"],
        date="date", ca="montant_eur", ca_label="Chiffre d'affaires (€)",
        id="ticket_id", decision="bon_reduction", decision_label="bon de réduction envoyé",
        resultat="revisite_30j", sensibles=["tranche_age", "genre", "region"], segment="canal",
        evenement=("2023-09-01", "hausse des prix de 8 %"), atypiques=[]),
}


def charger(secteur):
    """Renvoie (données brutes, configuration du secteur)."""
    cfg = CONFIG[secteur]
    df = pd.read_csv(fichier(cfg["fichier"]), parse_dates=cfg["dates"])
    return df, cfg


def reference():
    """Répartition de la population de référence (approximation pédagogique inspirée de l'INSEE)."""
    return pd.read_csv(fichier("reference_population.csv"))


def brief(secteur):
    """Affiche le brief du secteur dans le notebook."""
    from IPython.display import Markdown
    return Markdown(fichier(f"BRIEF_{secteur}.md").read_text(encoding="utf-8"))


def nettoyage_minimal(df, cfg):
    """Doublons exacts, âges impossibles et montants négatifs (avoirs) écartés de l'analyse."""
    out = df.drop_duplicates()
    if "age" in out:
        out = out[out["age"].isna() | (out["age"] >= 18)]
    out = out[out[cfg["ca"]] >= 0]
    return out.copy()


PALETTE = ["#0072B2", "#E69F00", "#009E73", "#CC79A7", "#56B4E9", "#D55E00", "#F0E442", "#000000"]  # Okabe-Ito, lisible par les daltoniens


def exporter_html(titre, blocs, chemin, sous_titre=""):
    """Assemble des figures Plotly et des blocs HTML en une page autonome (plotly.js inclus une fois).

    blocs : liste de chaînes HTML ou de tuples (titre, figure, description pour l'accessibilité).
    """
    import plotly.io as pio
    parties, premier = [], True
    for bloc in blocs:
        if isinstance(bloc, str):
            parties.append(bloc)
            continue
        t, fig, desc = bloc
        html = pio.to_html(fig, full_html=False, include_plotlyjs=premier,
                           config={"displaylogo": False, "responsive": True})
        premier = False
        parties.append(f'<section><h2>{t}</h2><p class="desc">{desc}</p>{html}</section>')
    style = """
    body{font-family:Arial,Helvetica,sans-serif;margin:0;background:#FAFAFA;color:#1B212C}
    header{background:#1B212C;color:#fff;padding:20px 32px}header h1{margin:0;font-size:26px}
    header p{margin:6px 0 0;color:#82C7A5}main{max-width:1100px;margin:0 auto;padding:16px 24px}
    section{background:#fff;border-radius:10px;padding:16px 20px;margin:16px 0;box-shadow:0 1px 3px rgba(0,0,0,.08)}
    h2{font-size:19px;margin:0 0 4px}.desc{color:#4E5567;margin:0 0 8px;font-size:15px}
    .alerte{border-left:6px solid #D55E00;background:#FFF4EC}.alerte li{margin:4px 0}
    .ok{border-left:6px solid #009E73}footer{color:#6B7385;font-size:13px;text-align:center;padding:16px}
    """
    page = (f'<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1"><title>{titre}</title>'
            f'<style>{style}</style></head><body><header><h1>{titre}</h1><p>{sous_titre}</p></header>'
            f'<main>{"".join(parties)}</main><footer>Données fictives à usage pédagogique</footer></body></html>')
    Path(chemin).write_text(page, encoding="utf-8")
    return Path(chemin).stat().st_size / 1e6
