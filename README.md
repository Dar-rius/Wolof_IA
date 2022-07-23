# Wolof IA

L’objectif est de créer plusieurs `dataset` sur des messages écrit en Wolof afin d'être utilisé pour entraîner des modèles de machine learning pour plusieurs raisons :

- Détecter les sentiments.
- Détecter la satisfaction d’une personne envers un produit.
- Détecter l'intérêt d’une personne envers un produit.

Les modèles seront ensuite exportés sous forme d’`API` pour être utilisé dans des projets nécessitant l’aide d’une IA.

[![Made-In-Senegal](https://github.com/GalsenDev221/made.in.senegal/blob/master/assets/badge.svg)](https://github.com/GalsenDev221/made.in.senegal)

## Description 📃

La plateforme est une application web développée avec le framework Django, dedans les  visiteurs devront entrer un ou plusieurs messages parlant d’un événement qui leur a marquer puis devront préciser l'émotion qu’ils ont ressenti sur cet événement entre positive ou négative, après tout ceci les messages seront enregistrer dans une base de donnée en `sqlite3` et extrait de la base de donnée pour entraîner un modèle de machine learning.  
Une fois le modèle entraîné, il sera exporté vers le serveur de l’application web pour être testé par les visiteurs du site.

## Exigence pour le développement ✅

### Application web 🌐

Pour travailler sur ce projet vous devez en premier installer :

``python (3.10+)`` et ``pip``

Et suivre les étapes suivantes ⬇️

#### 1 - Créer un environnement virtuel

Windows

```$ py -m venv wolof-ai_project```

Linux

```$ python3 -m venv wolof-ai_project```

Changer de répetoire

```$ cd wolof-ai_project```

#### 2 - Activer l'environnement

Windows

```$ Scripts\activate```

Linux

```$ source bin/activate```

#### 3 - Installation du projet

```bash
$ git clone https://github.com/Dar-rius/Wolof_IA.git

$ cd Wolof_IA
```

#### 4 - Installation des dépendances

Windows

``$ pip install -r requirements.txt``

Linux

```bash
# Installer libpq-dev
$ sudo apt install libpq-dev

# Installer les dependances
$ pip3 install -r requirements.txt
```

#### 5 - Executer le serveur

Windows

```$ py manage.py runserver```

Linux

```$ python3 manage.py runserver```

Dans votre navigateur tapez : ``localhost:8000``

#### 🛣️ Routes

Routes | Utilités
-------| -----------------------------------
accueil/  | Page d'accueil
messages/  | Liste des messages et leur labels
services/    |  Tester les modèles

#### ℹ️ Dossiers importants

Dossiers       | Utilités
---------------|------------------------------------
server         | Serveur de l'application web
message_wolof  | L'application web

### Machine Learning 🤖

En cours ...
> Arrivera une fois qu’il y aura suffisamment de données à traiter par les modèles.

## Contribution 🌍

Merci de votre intérêt pour ce projet, nous essayons de fournir un bon environnement de collaboration pour toutes les personnes impliquées.

Le projet est encore à ses débuts et seul l’application web est terminée.  
Pour contribuer vous pouvez alimenter la base de donnée via la plateforme en écrivant des messages en Wolof sur des événement qui vous ont marqués et en précisant l'émotion ressentie dans cet événement.

Signaler les problèmes que vous avez rencontrés en [ouvrant un Issue](https://github.com/Dar-rius/Wolof_IA/issues), si vous souhaitez améliorer la plateforme en ajoutant des sections, fonctionnalitées ou modifier la conception de la plate-forme nous vous recommandons [d’ouvrir un Issue](https://github.com/Dar-rius/Wolof_IA/issues) en précisant vos intentions, pour ne pas gaspiller votre temps. Vous pouvez également contribuer aux tâches qui sont actuellement en cours.  
Lorsque vous voudrez fusionner les modifications que vous avez réalisé au projet sur GitHub, ouvrez un [Pull Request](https://github.com/Dar-rius/Wolof_IA/pulls).

## License 🎫

Ce projet est sous Licence [MIT](License)
