import numpy as np
from fastapi import APIRouter, HTTPException
from joblib import load
from app.schemas.company_emissions import CompanyEmissions
from app.config.settings import settings
from app.utils.load_cluster_model import load_cluster_model

router = APIRouter()

classification_model = load(settings.models_path + settings.models_random_name + ".joblib")

# {
#   "eprtrSectorName": "Chemical industry", 
#   "pollutants": { "1,1,2,2-tetrachloroethane (TETRACHLOROETHANE-1,1,2,2)": 0.0, "1,2,3,4,5,6-hexachlorocyclohexane (HCH)": 0.0, "1,2-dichloroethane (DCE-1,2)": 3300.0, "Aldrin": 0.0, "Ammonia (NH3)": 0.0, "Anthracene": 0.0, "Arsenic and compounds (as As)": 0.0, "Asbestos": 0.0, "Benzene": 0.0, "Benzo(g,h,i)perylene": 0.0, "Brominated diphenylethers (PBDE)": 0.0, "CONFIDENTIAL": 0.0, "Cadmium and compounds (as Cd)": 0.0, "Carbon dioxide (CO2)": 0.0, "Carbon dioxide (CO2) excluding biomass": 0.0, "Carbon monoxide (CO)": 0.0, "Chlordecone": 0.0, "Chlorides (as total Cl)": 0.0, "Chlorine and inorganic compounds (as HCl)": 0.0, "Chlorofluorocarbons (CFCs)": 0.0, "Chromium and compounds (as Cr)": 0.0, "Copper and compounds (as Cu)": 0.0, "Di-(2-ethyl hexyl) phthalate (DEHP)": 0.0, "Dichloromethane (DCM)": 0.0, "Ethyl benzene": 0.0, "Ethylene oxide": 0.0, "Fine particulate matter (PM2.5)": 0.0, "Fluoranthene": 0.0, "Fluorides (as total F)": 0.0, "Fluorine and inorganic compounds (as HF)": 0.0, "Halogenated organic compounds (as AOX)": 0.0, "Halons": 0.0, "Hexachlorobenzene (HCB)": 0.0, "Hydro-fluorocarbons (HFCS)": 0.0, "Hydrochlorofluorocarbons (HCFCs)": 0.0, "Hydrogen cyanide (HCN)": 0.0, "Lead and compounds (as Pb)": 0.0, "Lindane": 0.0, "Mercury and compounds (as Hg)": 0.0, "Methane (CH4)": 0.0, "Naphthalene": 0.0, "Nickel and compounds (as Ni)": 0.0, "Nitrogen oxides (NOX)": 0.0, "Nitrous oxide (N2O)": 0.0, "Non-methane volatile organic compounds (NMVOC)": 0.0, "Nonylphenol and Nonylphenol ethoxylates": 0.0, "PCDD + PCDF (dioxins + furans) (as Teq)": 0.0, "Particulate matter (PM10)": 0.0, "Pentachlorobenzene": 0.0, "Pentachlorophenol (PCP)": 0.0, "Perfluorocarbons (PFCs)": 0.0, "Phenols (as total C)": 0.0, "Polychlorinated biphenyls (PCBs)": 0.0, "Polycyclic aromatic hydrocarbons (PAHs)": 0.0, "Sulphur hexafluoride (SF6)": 0.0, "Sulphur oxides (SOX)": 0.0, "Tetrachloroethylene": 0.0, "Tetrachloromethane (TCM)": 0.0, "Toluene": 0.0, "Total nitrogen": 0.0, "Total organic carbon(as total C or COD/3) (TOC)": 0.0, "Trichlorobenzenes (TCB)": 0.0, "Trichloroethylene (TRI)": 0.0, "Trichloromethane": 0.0, "Vinyl chloride": 0.0, "Xylenes": 0.0, "Zinc and compounds (as Zn)": 0.0}
# }

@router.post(
    "/classify",
    description="Attribue une note écologique à une entreprise.",
)
def classify(company_emissions: CompanyEmissions):
    try:
        cluster_model = load_cluster_model(company_emissions.eprtrSectorName)

        pollutants_array = np.array([[company_emissions.pollutants[pollutant] for pollutant in sorted(company_emissions.pollutants)]])
        
        cluster_label = cluster_model.predict(pollutants_array)

        input_for_classification = np.append(pollutants_array, cluster_label).reshape(1, -1)

        predicted_grade = classification_model.predict(input_for_classification)

        return {"predicted_grade": predicted_grade[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")