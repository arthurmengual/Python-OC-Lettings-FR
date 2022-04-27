## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
  `which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1`
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

**\***Vous aurez besoin d'avoir un compte sur les applications suivantes:**\***

- CIRCLECI: https://app.circleci.com/
- DOCKER: https://hub.docker.com/
- HEROKU: https://dashboard.heroku.com/
- SENTRY: https://sentry.io/

**\*** Pipeline circleci **\***

- Le pipeline circleci est réalisé grace à la configuration du fichier config.yml. Ce dernier détaille les étapes qui seront effectuées à chaque push d'une modification du code. Test et linting du code, creation d'une image docker et push de l'image sur docker hub. Pull de l'image et déploiement grâce à Heroku. Seul les push sur la branche master seront conteneurisé et déployés.

**\***les étapes nécessaires pour effectuer le déploiement **\***
1 - CircleCI: rendez vous sur l'application circleci et connectez votre repository github à votre espace circleci.

- Choisissez dans vos projet le projet que vous souhaitez déployer.
- Dans les variables d'environnement ajouter les vaiables suivantes:
  -DOCKER_PASSWORD: votre mot de passe docker

  -DOCKER_USERNAME: votre username docker

  -HEROKU_API_KEY: la clé de votre projet heroku

  -SECRET_KEY: la clé de votre application django

-Dans le fichier .circleci/config.yml remplacez oc-lettings-site29 par le nom de votre application configurée sur heroku. Remplacez le WORKING_DIRECTORY par votre dossier de travail, remplacez oc_lettings par le nom que vous souhaitez donner à votre image docker.

2- Heroku: rendez vous sur l'application Heroku et démarrez un nouveau projet que vous nommerez comme dans le fichier config.yml.
Dans les variables d'environnement ajoutez la variable suivante:
-SENTRY_DSN: votr clef sentry (vous la trouverez lors de la configuration de sentry)

3- Sentry: Rendez vous sur l'application sentry et démarrez un nouveau projet. Suivez les instruction en replaçant la configuration fournie avec la clef sentry dans les settings de votre application django.

4- Dans votre application créez un fichier caché .env dans lequel vous stockerez toutes les variables d'environnement que vous utiliserez en local. Dans votre fichier settings.py ajoutez un pont vers le fichier .env afin que vos clefs secrètes n'apparaissent pas sur votre repository public. Exemple de settings=> os.environ.get('SECRET_KEY', default='Foo'), os.environ.get('SENTRY_KEY), etc...

Voila! La configuration est établie pour le déploiement ;-), vous n'avez plus qu'à réaliser un push sur Git
du projet pour que le déploiement se fasse en automatique.
