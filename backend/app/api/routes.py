from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.translation_service import translate_text

router = APIRouter()


class TranslationRequest(BaseModel):
    text: str
    target_lang: str


@router.post("/translate")
def translate(request: TranslationRequest):

    try:
        result = translate_text(request.text, request.target_lang)
        return result

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))