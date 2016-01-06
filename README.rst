===============
bottle-drybones
===============

Template pour les projets bottle.

Prérequis
=========
pip, virtualenv, virtualenvwrapper et cookiecutter doivent être installés.

Procédure
=========
Pour générer un template pour le projet **myapp** :

Création de l'environnement virtuel
-----------------------------------

Pour créer l'environnement virtuel, se placer dans le répertoire d'installation du projet::

    $ mkvirtualenv myapp

Création du projet
-------------------

Pour créer le nouveau projet en utilisant le template::

    $ cookiecutter https://github.com/unistra/bottle-drybones.git

Configuration du projet
-----------------------

Pour configurer le projet dans l'environnement virtuel::

    $ cd myapp
    $ setvirtualenvproject $VIRTUAL_ENV $(pwd)

    # Edition du fichier postactivate
    $ echo "export SETTINGS_MODULE=myapp.settings.dev" >> $VIRTUAL_ENV/bin/postactivate

    # Edition du fichier postdeactivate
    $ echo "unset SETTINGS_MODULE" >> $VIRTUAL_ENV/bin/postdeactivate

    # Rechargement de l'environnement virtuel
    $ workon myapp

    # Installation de l'application pour le dev
    $ python setup.py develop

Installation des librairies
---------------------------

Pour installer les librairies ::

    $ cdproject
    $ pip install -r requirements/dev.txt

Lancer les tests
----------------

Pour tester l'installation: ::

    $ tox

Lancer le serveur
-----------------

Pour lancer le serveur: ::

    $ chaussette myapp.wsgi.application

Déploiement
-----------

Il faut utiliser pydiploy.
