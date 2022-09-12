<p align="center">
  <img src="https://user.oc-static.com/upload/2020/09/18/16004295603423_P11.png" />
</p>

**QA Branch :** [![CircleCI](https://circleci.com/gh/sebastiengiordano/Python-OC-Lettings-FR/tree/qa.svg?style=svg)](https://circleci.com/gh/sebastiengiordano/Python-OC-Lettings-FR/?branch=qa)

## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Python, version 3.9 ou supérieure

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
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

### Description générale

Le déploiement de l'application est automatisé grâce au pipeline CircleCI.
Quand une modification est poussée sur le dépôt GitHub, le pipeline s'active et déroule les étapes suivantes:

* Pour toutes les branches :
    * Création d'une image du projet
	* Réalisation des tests de linting avec flake8
	* Lancement de la suite de tests avec pytest
* Pour la branche QA uniquement, et si les tests ne remontent aucunes erreur :
	* Construction de l'image docker
	* Connection au dépôt DockerHub
	* Tag de l'image avec le hash de commit CircleCI
	* Publication de l'image sur le DockerHub
	* Connection à Heroku
	* Publication du conteneur dans le registre Heroku

### Paramétrage

Afin de pouvoir publier l'image sur le DockerHub puis sur Heroku des variables d'environnement doivent être créé.

Certaines sont spécifiques au projet, pour les créer, dans votre compte CircleCI, allez :

- Dans **Projets** :
- Cliquez sur `...` à droite du projet.
- Sélectionnez `Project Settings`.
- Dans `Environment Variables`,
- Ajoutez les variables avec `Add Environment Variables`.

Concernant les variables d'environnement qui correspodent aux identifiants DockerHub et Heroku, celle-ci peuvent être utilisé dans l'ensemble de vos projets.
Pour se faire, dans votre compte CircleCI, allez :

- Dans **Organization Settings**,
- puis dans **Contexts** :
- Cliquez sur `Create context` (puis créez docker-env-var et heroku-env-var).
- Dans ces contexts, ajoutez les variables d'environnement avec `Add Environment Variables`.


 |   Nom des Variables  |   Description   |   Commentaire   |
|---    |---   |
|   DOCKER_ID   |   Nom de votre compte DockerHub   |   Disponible sous "docker-env-var"   |
|   DOCKER_PWD   |   Mot de passe de votre compte DockerHub   |   Disponible sous "docker-env-var"   |
|   HEROKU_TOKEN |  Clef Heroku  |   Disponible sous "heroku-env-var"   |
| SENTRY_DSN    | URL Sentry  |   Disponible sous "Project Settings"   |
| HEROKU_APP_NAME | Le nom de l'application |   Disponible sous "Project Settings"   |

## Ligne de commande utile

### Docker

Afin de récupérer l'image Docker créé lors du déploiement, utiliser la commande suivante :
```sh
docker pull <DOCKER_ID>/oc-lettings:lastest
```

Ensuite, pour démarrer le conteneur :
```sh
docker run -d -e "PORT=8000" -p 2368:8000 <DOCKER_ID>/oc-lettings:lastest
```

Vous pourrez ainsi accéder au site danns un navigateur à l'adresse :
```sh
http://localhost:2368/
```
ou
```sh
http://127.0.0.1:2368/
```

(Remarque: vous pouvez remplacer le port `2368` par celui de votre choix)


### Heroku

Afin de générer votre clef Heroku (HEROKU_TOKEN) :

```sh
heroku authorizations:create
```

Pour accéder à votre site :

```sh
heroku apps:open -a <HEROKU_APP_NAME>
```

## Logging

Afin de collecter les anomalies, le module Sentry-sdk est configuré.
