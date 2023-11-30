# Index d'impact environnemental

## Introduction
             
Projet DATA de fin d'année inscrit à la formation RNCP 36286 de niveau 7, *Expert en informatique et en systèmes d'informations*.               

Avec les évolutions constatées du changement climatique au niveau planétaire, il apparaît clairement que l’un des enjeux majeurs de notre époque sera de limiter l'impact négatif de notre activité sur l'environnement.                

Avec la prise de conscience écologique, les investisseurs et les décideurs souhaitent faire plus attention à leurs actions. Ce projet permet ainsi d'attribuer une note écologique en comparant les relevés d'émissions de polluants des entreprises d'un même secteur entre elles.             


## Installation

- Vous devez avoir la version 3.11 de python           
- `pip install pipenv`           
- `pipenv shell`        
- `pipenv install`                              
- `pipenv run start`                        

Le dossier *modules* contient les notebooks qui nous ont servi à l'exploration des données et à l'entrainement des algorithmes de machine learning.         

Le dossier *app* contient l'api réalisée avec le framework *fastapi*.       
Le point d'entrée de l'api est le fichier *main.py*.         
Les endpoints sont définis dans le dossier *routers*.         

Les endpoints définis sont :       
- */api/save_file*, qui permet d'uploader le fichier F1_4 depuis son système de fichiers local.       
- */api/train_models*, qui entraine les modèles KMeans et RandomForestClassifier avec les données du fichier F1_4.         
- */api/classify*, qui attribue une note à une entreprise en fonction des paramètres d'entrée.      

Exemple de données en entrée pour */api/classify* :         
```json
{
   "eprtrSectorName": "Chemical industry", 
   "pollutants": { 
        "1,1,2,2-tetrachloroethane (TETRACHLOROETHANE-1,1,2,2)": 0.0, "1,2,3,4,5,6-hexachlorocyclohexane (HCH)": 0.0, "1,2-dichloroethane (DCE-1,2)": 3300.0, "Aldrin": 0.0, "Ammonia (NH3)": 0.0, "Anthracene": 0.0, "Arsenic and compounds (as As)": 0.0, "Asbestos": 0.0, "Benzene": 0.0, "Benzo(g,h,i)perylene": 0.0, "Brominated diphenylethers (PBDE)": 0.0, "CONFIDENTIAL": 0.0, "Cadmium and compounds (as Cd)": 0.0, "Carbon dioxide (CO2)": 0.0, "Carbon dioxide (CO2) excluding biomass": 0.0, "Carbon monoxide (CO)": 0.0, "Chlordecone": 0.0, "Chlorides (as total Cl)": 0.0, "Chlorine and inorganic compounds (as HCl)": 0.0, "Chlorofluorocarbons (CFCs)": 0.0, "Chromium and compounds (as Cr)": 0.0, "Copper and compounds (as Cu)": 0.0, "Di-(2-ethyl hexyl) phthalate (DEHP)": 0.0, "Dichloromethane (DCM)": 0.0, "Ethyl benzene": 0.0, "Ethylene oxide": 0.0, "Fine particulate matter (PM2.5)": 0.0, "Fluoranthene": 0.0, "Fluorides (as total F)": 0.0, "Fluorine and inorganic compounds (as HF)": 0.0, "Halogenated organic compounds (as AOX)": 0.0, "Halons": 0.0, "Hexachlorobenzene (HCB)": 0.0, "Hydro-fluorocarbons (HFCS)": 0.0, "Hydrochlorofluorocarbons (HCFCs)": 0.0, "Hydrogen cyanide (HCN)": 0.0, "Lead and compounds (as Pb)": 0.0, "Lindane": 0.0, "Mercury and compounds (as Hg)": 0.0, "Methane (CH4)": 0.0, "Naphthalene": 0.0, "Nickel and compounds (as Ni)": 0.0, "Nitrogen oxides (NOX)": 0.0, "Nitrous oxide (N2O)": 0.0, "Non-methane volatile organic compounds (NMVOC)": 0.0, "Nonylphenol and Nonylphenol ethoxylates": 0.0, "PCDD + PCDF (dioxins + furans) (as Teq)": 0.0, "Particulate matter (PM10)": 0.0, "Pentachlorobenzene": 0.0, "Pentachlorophenol (PCP)": 0.0, "Perfluorocarbons (PFCs)": 0.0, "Phenols (as total C)": 0.0, "Polychlorinated biphenyls (PCBs)": 0.0, "Polycyclic aromatic hydrocarbons (PAHs)": 0.0, "Sulphur hexafluoride (SF6)": 0.0, "Sulphur oxides (SOX)": 0.0, "Tetrachloroethylene": 0.0, "Tetrachloromethane (TCM)": 0.0, "Toluene": 0.0, "Total nitrogen": 0.0, "Total organic carbon(as total C or COD/3) (TOC)": 0.0, "Trichlorobenzenes (TCB)": 0.0, "Trichloroethylene (TRI)": 0.0, "Trichloromethane": 0.0, "Vinyl chloride": 0.0, "Xylenes": 0.0, "Zinc and compounds (as Zn)": 0.0
    }
}
```           

Le dossier F1_4 peut être trouvé sur ce [lien](https://sdi.eea.europa.eu/data/3da7d329-beea-4a7b-89bc-d45fc1c4b8ac?path=%2FCSV).          

Dans le dossier *datasets/european_companies/CSV* à la racine du projet, les différents fichiers .csv doivent être présents, ces fichiers peuvent être trouvés sur ce [lien](https://sdi.eea.europa.eu/data/3da7d329-beea-4a7b-89bc-d45fc1c4b8ac?path=%2FCSV).       


## Liens                  
- [Régulation des polluants dans l'UE](https://www.breeze-technologies.de/blog/european-eu-regulation-and-limits-on-air-pollution/)                                        
- [GBS](https://www.cdc-biodiversite.fr/publications/global-biodiversity-score-update2021-cahier18/)                  