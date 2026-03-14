from app.models.model_manager import ModelManager
from app.utils.language_utils import detect_language
from app.utils.text_utils import split_text
from app.services.translation_memory import get_translation, save_translation

model_manager = ModelManager()

def translate_text(text, target_lang):

    source_lang = detect_language(text)

    # Check translation memory
    cached_translation = get_translation(text, source_lang, target_lang)

    if cached_translation:
        return {
            "source_language": source_lang,
            "translation": cached_translation,
            "from_memory": True
        }

    model_data = model_manager.get_model(source_lang, target_lang)

    tokenizer = model_data["tokenizer"]
    model = model_data["model"]

    chunks = split_text(text)

    tokens = tokenizer(chunks, return_tensors="pt", padding=True, truncation=True)

    translated = model.generate(**tokens)

    translated_chunks = [
        tokenizer.decode(t, skip_special_tokens=True)
        for t in translated
    ]

    final_translation = " ".join(translated_chunks)

    # Save translation in memory
    save_translation(text, source_lang, target_lang, final_translation)

    return {
        "source_language": source_lang,
        "translation": final_translation,
        "from_memory": False
    }