<table>
  <tr>
    <td><img src="Screenshots/1.png" alt="1"></td>
    <td><img src="Screenshots/2.png" alt="2"></td>
    <td><img src="Screenshots/3.png" alt="3"></td>
  </tr>
  <tr>
    <td><img src="Screenshots/4.png" alt="4"></td>
    <td><img src="Screenshots/5.png" alt="5"></td>
  </tr>
</table>

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
$cd projet1-grp_e8
$python3 -m venv venv
$source venv/bin/activate
$pip install -r requirements.txt
$python3 app.py
```

## **Description du projet**

L’objectif de l’application est de faciliter le vote en donnant un accès facile au programme de chaque candidat et en proposant une première analyse du programme qui pourra être affinée par les citoyens les plus investis. Ensuite la localisation des différents bureaux de vote facilite la démarche de vote pour les personnes les plus récalcitrantes.

### **Fonctions de l'application**

* Chaque candidat aura des identifiants pour pouvoir se connecter et rentré leur programme en ligne.
* Ensuite après le référencement d’un programme, une analyse automatique permet de « noter » suivant plusieurs critères le candidats (critère écologique, sociale, économique et juridique). Cette notation permet ensuite d’afficher 4 barres sur le site internet plus ou moins remplie (pourcentage de remplissage).
* Chaque citoyen peut ensuite influer sur ces notations (dans la limite d’une variation de +- 5%) après avoir lu le programme d’un candidat (permet d’avoir un avis plus large sur la perception du candidat).
* Système de localisation des différents bureaux de vote pour faciliter le vote de chacun.
