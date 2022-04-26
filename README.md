# Créez une API sécurisée RESTful en utilisant Django REST.
## Descriptif
**SoftDesk** est une API sécurisée RESTful permettant de remonter et suivre des problèmes techniques (issue tracking system).

L'application permet essentiellement aux utilisateurs de créer divers projets, d'ajouter des collaborateurs à des projets spécifiques, de créer des problèmes au sein des projets et d'attribuer des libellés à ces problèmes en fonction de leurs priorités, de balises, etc ...

L'application exploite les points de terminaison d'API qui servent les données.

## Documentation

* Lien vers la documentation Postman de l'API, contenant des détails sur chaque point de terminaison : <https://documenter.getpostman.com/view/20587842/Uyr8nJYx>

## Prérequis
* Python 3.9 ( lien de téléchargement: <https://www.python.org/downloads>)

## Installation de l'application

* Récupérer les livrables du projet sur votre poste de travail en téléchargant le dossier **OpenclassroomsProject10-main** depuis ce lien [GitHub](https://github.com/SelHel/OpenclassroomsProject10.git) ou en clonant le dépôt en utilisant le terminal sous Mac/Linux ou l'invite de commandes sous Windows :<br>

	```
	git clone https://github.com/SelHel/OpenclassroomsProject10.git
	```

* Ensuite, placez vous dans le dossier "OpenclassroomsProject10" et créez un environnement virtuel :

	```
	python -m venv <your-virtual-env-name>
	```

* Activez votre environnement virtuel :

	```
	<your-virtual-env-name>\Scripts\activate.bat (sous Windows)
	```
	ou
	
	```
	source <your-virtual-env-name>/bin/activate (sous Mac/Linux)
	```

* Installer les dépendances avec la commande suivante :

	```
	pip install -r requirements.txt
	```
## Exécution de l'application
* Pour exécuter l'application toujours dans le terminal sous Mac/Linux ou l'invite de commandes sous Windows lancez le serveur de développement en utilisant la commande :

	```
	python manage.py runserver
	```

* Pour accéder à la page d'accueil et naviguer dans l'application coller cette adresse dans votre navigateur :
	
	```
	http://127.0.0.1:8000/
	```
* Pour accéder au site d'administration de Django et pouvoir effectué des opérations CRUD coller cette adresse dans votre navigateur :

	```
	 http://127.0.0.1:8000/admin/
	```
* Connectez-vous en utilisant le nom d'utilisateur "admin" et le mot de passe "admin".

## Auteur
**Selim Helaoui**