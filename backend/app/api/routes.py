from fastapi import APIRouter
from app.services.translation_service import translate_text

router = APIRouter()

@router.post("/translate")
def translate(text: str):
    result = translate_text(text)
    return {"translation": result}