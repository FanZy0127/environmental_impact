from pydantic import BaseModel
from typing import Dict


class CompanyEmissions(BaseModel):
    eprtrSectorName: str
    pollutants: Dict[str, float]