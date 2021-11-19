# PPII «Projet Pluridisciplinaire d'Informatique Intégrative» 1 (2021-2022)

Olivier Festor <<olivier.festor@telecomnancy.eu>>  
Gérald Oster <<gerald.oster@telecomnancy.eu>>  


## Démocratie Participative

[Le sujet détaillé est disponible en version PDF](./Projet_2021_DP.pdf)

**Membres du groupe** :  

* CHENEVIERE Thibault <<thibault.cheneviere@telecomnancy.eu>>  
* GUILLOT Thom <<thom.guillot@telecomnancy.eu>>  
* HASHANI Elion <<elion.hashani@telecomnancy.eu>>  
* YEBOUET Antoine <<antoine.yebouet@telecomnancy.eu>>  

## Description du projet

### Fonctions principales

* Page de News de la ville (en page d'accueil) avec les news des clubs de la ville (sportif, artistique, culturel, …), nouvelle décision des élus (projets qui ont été acceptés).  
* Système d’aide à la prise de décision : avant de voter un projet, permettre au citoyen de choisir le budget alloué à ce projet, impliquer les citoyens sur les plans urbains de la ville à travers des sondages (les mineurs ne pourront pas voter et il y a un vote unique par personne) et des discussions.  
* Système lors d'élection : présenter les programmes des différents candidats à travers un hémicycle (représentation graphique) qui répertorie tous les candidats. Les candidats écriront directement leur programme pour éviter les informations biaisées.  
* Système d’entraide entre les riverains : faire une plateforme pour poster ses annonces pour demander de l’aide ou proposer son aide (par exemple aide pour faire du bricolage, de la mécanique, aide sur un problème avec du matériel informatique, …).  
* Système de création de projet par les citoyens : système de budget participatif (possibilité de financer des projets de riverains) et possibilité de promouvoir un projet avec des pétitions pour les faire connaître et financer par les élues.
Système de signalisation des problèmes : chaque citoyen peut signaler des incivilités ou des problèmes liés à la gestion de la ville (problème de circulation sur certains axes, problème de ramassage des poubelles dans certains quartiers, …)  

### Première description du fonctionnement de l’application

Site web avec une base de login/signup :  

* Pour le signup, vérification de l’identité via :  
  * Vérification de la carte d’identité  
  * Vérification des informations personnelles (Prénom, nom, adresse, âge, sexe, adresse IP, eMail)  
* Chaque personne peut créer un compte librement (but de toucher un maximum de personne)  
* Possibilité de supprimer ses informations personnelles en se désinscrivant mais les messages et discussion postés/créés resteront sur le site (pour des raisons de logique du débat). Néanmoins, le nom de l’auteur sera retiré de toutes les publications et remplacé par « Anonyme » ou « Désinscrit ».  
* Envoi d’un mail de confirmation pour valider l’adresse mail.
