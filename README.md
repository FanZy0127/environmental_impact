# Index d'impact environnemental

## TODO 

- Regarder partie 3.3 de https://sdi.eea.europa.eu/data/3da7d329-beea-4a7b-89bc-d45fc1c4b8ac?dir=undefined&path=%2FDOCUMENTATION&openfile=5704828             
- A cette adresse il y a également un dataset avec les entreprises qui sont flag en tant qu'"anomalies"         
- On peut analyser les tendances au fil du temps et prédire les futures performances environnementales ou les besoins de conformité, via un modèle LSTM par exemple. Peut servir pour de la planification stratégique et prévision des exigences de conformité environnementale.                
- Prédire la quantité d'émissions basées sur différentes caractéristiques des installations via de la régression linéaire, régression ridge, LASSO. Doit permettre de prédire l'impact environnemental des installations, ce qui peut être utilisé pour la planification de la conformité et la gestion des risques.            
- Classer les installations en différentes catégories de risque environnemental ou de performance. Arbres de décision, forêts aléatoires, machines à vecteurs de support (SVM), réseaux de neurones. Identifier les installations nécessitant une surveillance réglementaire accrue ou des audits environnementaux.              
- Regrouper des installations similaires pour identifier des modèles ou des comportements. K-means, clustering hiérarchique, DBSCAN. Découverte de groupes d'installations avec des caractéristiques opérationnelles ou environnementales similaires pour des interventions ciblées.             

Détection d'anomalies :

    Objectif : Identifier les comportements d'exploitation anormaux ou les données aberrantes qui pourraient indiquer des erreurs de déclaration ou des problèmes de conformité.
    Algorithmes : Isolation Forest, Local Outlier Factor (LOF), One-Class SVM.
    Usage professionnel : Surveillance de la conformité et détection précoce des problèmes environnementaux.

## Introduction
             
Il s'agit du projet de fin d'année d'une formation RNCP de niveau 7, **Expert en informatique et des systèmes d'informations**.     
              
Avec les évolutions constatées du changement climatique au niveau planétaire, il apparaît clairement que l’un des enjeux majeurs de notre époque sera de limité l'impact négatif de notre activité sur l'environnement. 

Avec ce projet, nous voulons ainsi mesurer cet impact via différent indicateurs comme la qualité de l'air, la contamination des sols, la pollution de l'eau, et.... Pour cela, nous nous servons d'algorithmes de machine learning pour prédire l'évolution de la quantité de polluants et de la classification pour mesurer le degré de menace.


## Installation

- `source venv/bin/activate` or `venv/Scripts/activate`     
- `pip install -r requirements.txt`      
- `pip freeze > requirements.txt`       
                
Dans un dossier datasets à la racine du projet, uploadez les différents fichiers .csv que vous pourrez trouver via ce [lien](https://www.eea.europa.eu/data-and-maps/data/industrial-reporting-under-the-industrial-7).


## Démarche

Après avoir récupéré notre dataset, nous avons pris du temps pour l'étudier en commencant par les émissions de polluants pour environ 29223 entreprise européenne.           


## Liens
- [Régulation des polluants dans l'UE](https://www.breeze-technologies.de/blog/european-eu-regulation-and-limits-on-air-pollution/)               
- [GBS](https://www.cdc-biodiversite.fr/publications/global-biodiversity-score-update2021-cahier18/)           