import os
import uuid
import shutil
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from typing import Optional
from app.models.upload_models import UploadResponse
from app.services.upload_service import process_upload, TEMP_DIR

router = APIRouter(prefix="/upload", tags=["upload"])

@router.post("/", response_model=UploadResponse)
async def upload_file(
    file: UploadFile = File(...),
    mode: str = Form(...),
    session_id: Optional[str] = Form(None),
    incognito: bool = Form(False)
):
    if not session_id:
        session_id = str(uuid.uuid4())

    temp_path = os.path.join(TEMP_DIR, f"{uuid.uuid4()}_{file.filename}")

    try:
        with open(temp_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        result = process_upload(
            file_path=temp_path,
            filename=file.filename,
            mode=mode,
            session_id=session_id,
            incognito=incognito
        )

        return UploadResponse(
            success=True,
            filename=result["filename"],
            chunks_created=result["chunks_created"],
            collection=result["collection"],
            message=f"Successfully processed {file.filename}"
        )

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)