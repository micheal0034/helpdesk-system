import os
import uuid
import shutil
from fastapi import APIRouter, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse
from app.models.schemas import HelpRequest, HelpResponse, ClassificationResult, RetrievalResult
from app.services.helpdesk import process_helpdesk_request
from app.services.classifier import classify_request
from app.services.retriever import retrieve_knowledge
from app.retrieval.indexer import Indexer
from app.core.config import settings

router = APIRouter()
UPLOAD_DIR = settings.DATA_DIR 
indexer = Indexer(data_dir=settings.DATA_DIR, index_path=settings.INDEX_PATH)

@router.post("/classify", response_model=ClassificationResult)
def classify(req: HelpRequest):
    try:
        return classify_request(req.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/retrieve", response_model=list[RetrievalResult])
def retrieve(req: HelpRequest, k: int = 5):
    try:
        return retrieve_knowledge(req.text, k=k)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/helpdesk", response_model=HelpResponse)
def helpdesk(req: HelpRequest, k: int = 5):
    try:
        return process_helpdesk_request(req.text, k)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
