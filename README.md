# Projet : Calculatrice Web (LOG3000)

Version améliorée et documentée du projet de calculatrice web réalisé
dans le cadre du cours LOG3000. Ce dépôt contient une petite application
Flask qui évalue des expressions binaires simples envoyées depuis une
interface web.

**Équipe :** #12

## But et portée

Le but est de construire une application web de calculatrice simple tout en appliquant de bonnes pratiques GitHub.

- La gestion de versions et de code en équipe
- La documentation du dépôt Github et du code de base
- Réaliser des pipelines de tests
- Faire de la correction de bogues

La portée du projett est purement dans un cadre pédagogique.

## Prérequis

- Python 3.8+ installé
- pip

## Instructions d’installation

1. Cloner le dépôt :

```powershell
git clone https://github.com/alexphng/TP3-LOG3000.git
cd TP3-LOG3000
```

2. Créer et activer un environnement virtuel (recommandé) :

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Installer les dépendances :

```powershell
pip install -r requirements.txt
```

4. Lancer l'application en local :

```powershell
python app.py
```

L'application écoute par défaut sur http://127.0.0.1:5000/.

## Utilisation

- Ouvrir la page d'accueil dans un navigateur.
- Utiliser les boutons pour construire une expression.
- Appuyer sur '=' pour envoyer l'expression au serveur. Le résultat
  (ou un message d'erreur) s'affiche dans le champ d'affichage.

Remarques importantes :

- Seule une opération binaire est acceptée à la fois (ex. "1+2+3"
  est interdit).

## Tests

Les tests unitaires du projet utilisent le module intégré **unittest** de Pythin.
Ils sont situés dans le dossier /tests et couvrent les principales fonctionnalités de l’application :
- `test_calculate.py` : Vérifie la logique de la fonction `calculate()` dans `app.py`.
- `test_operators.py` : Vérifie les opérations arithmétiques (`add`, `subtract`, `multiply`, `divide`) dans `operators.py`.

### Exécuter tous les tests

```powershell
python -m unittest discover -v tests
```

## Structure du projet

- `app.py` — application Flask et fonction `calculate` qui parse les
  expressions.
- `operators.py` — fonctions arithmétiques utilisées par `calculate`.
- `templates/` — templates HTML (interface utilisateur).
- `tests/` — tests unitaires du projet
- `static/` — ressources statiques (CSS, images).
- `README.md` — ce fichier.

Chaque dossier contient son propre
`README.md` décrivant son rôle et les fichiers importants.

## Flux de contribution

- Branche principale : `main`.
- Nouvelles fonctionnalités ou corrections : créer une branche nommée
  `feature/xxx` ou `fix/xxx`.
- Ouvrir une Pull Request (PR) ciblant `main`. Inclure une description
  claire du changement et des étapes pour tester.
- Utiliser les issues pour signaler les bogues ou proposer des
  améliorations.
