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

Pour travailler sur ce vous devez avoir ceci:

``python (3.0+)``

#### Installation du projet

```
git clone https://github.com/Dar-rius/Wolof_IA.gi
cd Wolof_IA
```

#### Installation des libraries

``pip install -r requirements.txt``

````
# Windows:
py manage.py runserver 

# Linux:
python3 manage.py runserver

# MacOS:
python manage.py runserver 
````

Dans votre navigateur copier et coller ceci:
``localhost:8000``
