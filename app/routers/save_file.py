import pandas as pd
from io import BytesIO
from fastapi import APIRouter, File, UploadFile, HTTPException
from app.config.settings import settings

router = APIRouter()

@router.post(
    "/save_file",
    description="Upload en local des datasets.",
)
def save_file(file: UploadFile = File(..., media_type="text/csv")):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Invalid file format. Only CSV files are accepted.")

    try:
        contents = file.file.read()

        df = pd.read_csv(BytesIO(contents))

        required_columns = [
            "countryName", "EPRTRSectorCode", "eprtrSectorName",
            "EPRTRAnnexIMainActivityCode", "EPRTRAnnexIMainActivityLabel",
            "FacilityInspireID", "facilityName", "facilityNameConfidentialityReason",
            "Longitude", "Latitude", "addressConfidentialityReason", "City",
            "targetRelease", "pollutant", "emissions", "reportingYear",
            "releasesConfidentialityReason"
        ]

        if not all(column in df.columns for column in required_columns):
            raise ValueError("Missing required columns in the file.")
        
        if not all(df["targetRelease"] == "AIR"):
            raise ValueError("'targetRelease' must only contain 'AIR'.")

        df.to_csv(settings.files_path + file.filename, index=False)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}"}