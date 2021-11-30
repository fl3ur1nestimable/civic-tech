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

**Guide d'intallation rapide** :  

``` bash
$git clone https://gitlab.telecomnancy.univ-lorraine.fr/ppii2k22/project1-grp_e8.git
$cd projet1-grp_e8
$python3 -m venv venv
$source venv/bin/activate
$pip install -r requirements.txt
$python3 main.py
```

## **Description du projet**

L’objectif de l’application est de faciliter le vote en donnant un accès facile au programme de chaque candidat et en proposant une première analyse du programme qui pourra être affinée par les citoyens les plus investis. Ensuite la localisation des différents bureaux de vote facilite la démarche de vote pour les personnes les plus récalcitrantes.

### **Fonctions de l'application**

* Chaque candidat aura des identifiants pour pouvoir se connecter et rentré leur programme en ligne.
* Ensuite après le référencement d’un programme, une analyse automatique permet de « noter » suivant plusieurs critères le candidats (critère écologique, sociale, économique et juridique). Cette notation permet ensuite d’afficher 4 barres sur le site internet plus ou moins remplie (pourcentage de remplissage).
* Chaque citoyen peut ensuite influer sur ces notations (dans la limite d’une variation de +- 5%) après avoir lu le programme d’un candidat (permet d’avoir un avis plus large sur la perception du candidat).
* Système de localisation des différents bureaux de vote pour faciliter le vote de chacun.

### To do List  

* Faire le système de notation des programmes par mots-clés (utilisation d’un dictionnaire pondéré par critère pour noter le programme)  
* Faire l’interface utilisateur pour modifier la note d’un programme sur le site (vérifier que l’utilisateur a lu le programme, et modification unique de la note du programme)  
* Faire l’interface d’affichage des programme (liste de tous les programmes en grid) et affichage du programme détaillé avec les membres de la liste et les différentes notation du programme  
* Faire la page home avec une explication du fonctionnement du site et un exemple pour se familiariser avec le système de notation  
* Faire la page avec l'hémicycle : hémicycle statique avec en dessous en colonne en dessous de la tendance politique la liste des candidats cliquable pour arriver sur leur programme (faire des sortes de carte pour les candidats avec leur photo, nom, notations dans les différents domaines, parti politique)  
* Système de localisation du bureau de vote le plus proche (par form en demandant l’adresse de la personne ou en utilisant l’adresse IP)
