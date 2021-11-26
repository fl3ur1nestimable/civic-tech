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
$python3 -m venv /path/to/new/virtual/environment
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
