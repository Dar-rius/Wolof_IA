# Wolof IA

The objective is to curate multiple datasets based on Wolof-language messages to train machine learning models for several purposes:

- Sentiment analysis.
- Detecting user satisfaction with a product.
- Detecting user interest in a product.

These models will then be deployed as APIs to be integrated into projects requiring AI capabilities.

[![Made-In-Senegal](https://github.com/GalsenDev221/made.in.senegal/blob/master/assets/badge.svg)](https://github.com/GalsenDev221/made.in.senegal)

## Description 📃

The platform is a Django-based web application. Users input messages describing memorable events and label them as either 'positive' or 'negative'. This data is persisted in a `sqlite3` database and subsequently processed to train a machine learning model.  
Once trained, the model is deployed to the server, allowing site visitors to test its inference capabilities in real-time.

## Development Requirements ✅

### Web Application 🌐

To work on this project, you must first install:

``python (3.10+)`` et ``pip``

And follow the steps below ⬇️ 


#### 1 - Create a virtual environment

Windows

```$ py -m venv wolof-ai_project```

Linux

```$ python3 -m venv wolof-ai_project```

Change directory

```$ cd wolof-ai_project```


#### 2 - Activate environment

Windows

```$ Scripts\activate```

Linux

```$ source bin/activate```

#### 3 - Clone repos

```bash
$ git clone https://github.com/Dar-rius/Wolof_IA.git

$ cd Wolof_IA
```


#### 4 - Install dependecies

Windows

``$ pip install -r requirements.txt``

Linux

```bash
# Installer libpq-dev
$ sudo apt install libpq-dev

# Installer les dependances
$ pip3 install -r requirements.txt
```

#### 5 - Run server

Windows

```$ py manage.py runserver```

Linux

```$ python3 manage.py runserver```

In your browser, enter the following: ``localhost:8000``

#### 🛣️ Routes

Routes | Utilies
-------| -----------------------------------
accueil/  | Home Page
messages/  | List of messages and their labeles
services/    |  Use models for projects
test/    |  Testd models

#### ℹ️ Dossiers importants

Dossiers       | Utilities
---------------|------------------------------------
server         | Backend
message_wolof  | Frontend
machine_leaning| Machine Learning models

## Contribution 🌍

Thank you for your interest in this project. We strive to provide a collaborative environment for everyone involved.

The project is in its early stages, and only the web application is currently complete. 
To contribute, you can populate the database via the platform by submitting Wolof messages regarding memorable events and labeling the associated sentiment

Report any issues you encounter by [ouvrant un Issue](https://github.com/Dar-rius/Wolof_IA/issues), If you wish to improve the platform by adding sections, features, or modifying the design, we recommend [d’ouvrir un Issue](https://github.com/Dar-rius/Wolof_IA/issues) first to detail your intentions and avoid wasted effort. You can also contribute to tasks currently in progress. When you are ready to merge your changes into the project on GitHub, please open a [Pull Request](https://github.com/Dar-rius/Wolof_IA/pulls).

## License 🎫

This project use the [MIT](License) license
