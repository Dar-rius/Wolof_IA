# Wolof IA

L’objectif est de créer plusieurs dataset sur des messages écrit en wolof afin d'être utilisé pour entraîner des modèles de machine pour plusieurs raisons:
1. Détecter les sentiments.
2. Détecter la satisfaction d’une personne envers un produit. 
3. Détecter l'intérêt d’une personne envers un produit.

Les modèles seront ensuite exportés sous forme d’API pour être utilisé dans des projets nécessitant l’aide d’une IA. 

## Description

La plateforme est une application web développée avec le framework django, dedans les  visiteurs devront entrer un ou plusieurs messages parlant d’un événement qui leur a marquer puis devront préciser l'émotion qu’ils ont ressenti sur cet événement entre positive ou négative, après tout ceci les messages seront enregistrer dans une base de donnée en sqlite3 et extrait de la base de donnée pour entraîner un modèle de machine learning. 
Une fois le modèle entraîné, il sera exporté vers le serveur de l’application web pour être testé par les visiteurs du site.

## Exigence pour le developpement 

### Application web

Pour travailler sur ce projet vous devez avoir ceci:

``python (3.10+)``

#### Créer un environnement virtuel

Windows

```$ py -m venv wolof_ia```
 
Linux

```$ python3 -m venv wolof_ia```

Changer de repetoire

```$ cd message_wolof```
 
Activer l'environnement

Windows

```$ Scripts\activate```
 
Linux et MacOS

```$ source bin/activate```

#### Installation du projet

```
$ git clone https://github.com/Dar-rius/Wolof_IA.git

$ cd Wolof_IA
```

#### Installation des libraries

``$ pip install -r requirements.txt``

#### Executer le serveur

Windows

```$ py manage.py runserver ```

Linux

```$ python3 manage.py runserver```

Dans votre navigateur tapez  ceci:
``localhost:8000``

#### Routes

Routes | Utilités
-------| -----------------------------------
home/  | Page d'accueille
data/  | Liste des messages et leur labels
ia/    |  Tester les modeles

### Machine Learning

En cours 
> Arrivera une fois qu’il y aura suffisamment  de données dont les modèles devront traités

## Contribution

Merci de votre intérêt pour ce projet, nous essayons de fournir un bon environnement de collaboration pour toutes les personnes impliquées.

Le projet est encore à ses débuts et seul l’application web est terminée. Pour contribuer vous pouvez alimenter la base de donnée via la plateforme en écrivant des messages en wolof sur des événement qui vous ont marqués et en précisant l'émotion ressentie dans cet événement. 

Signaler les problèmes que vous avez rencontrés en [ouvrant un issue](https://github.com/Dar-rius/Wolof_IA/issues), si vous souhaitez améliorer la plateforme en ajoutant des sections, fonctionnalitées ou modifier la conception de la plate-forme nous vous recommandons [d’ouvrir un issue](https://github.com/Dar-rius/Wolof_IA/issues) en précisant vos intentions, pour ne pas gaspiller votre temps. Vous pouvez également contribuer aux tâches qui sont actuellement en cours.
Lorsque vous voudrez fusionner les modifications que vous avez réalisé au projet sur github, ourez un [pull request](https://github.com/Dar-rius/Wolof_IA/pulls).

## Licence
La licence utilisée est celle de [MIT](https://github.com/Dar-rius/Wolof_IA/blob/main/licence)
