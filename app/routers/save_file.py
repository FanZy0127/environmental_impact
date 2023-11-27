from fastapi import APIRouter, File, UploadFile, HTTPException
from app.config.settings import settings

router = APIRouter()

@router.post(
    "/save_file",
    description="Upload en local des datasets.",
)
def save_file(file: UploadFile = File(..., media_type="text/csv")):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Invalid file format. Only CSV files are accepted.")

    try:
        contents = file.file.read()
        with open(settings.files_path + file.filename, "wb") as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}"}