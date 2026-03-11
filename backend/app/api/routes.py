from fastapi import APIRouter
from pydantic import BaseModel
from app.services.translation_service import translate_text

router = APIRouter()

class TranslationRequest(BaseModel):
    text: str
    target_lang: str


@router.post("/translate")
def translate(request: TranslationRequest):

    result = translate_text(
        request.text,
        request.target_lang
    )

    return result