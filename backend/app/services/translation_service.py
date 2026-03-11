from app.models.model_manager import ModelManager
from app.utils.language_utils import detect_language

model_manager = ModelManager()

def translate_text(text, target_lang):

    source_lang = detect_language(text)

    model_data = model_manager.get_model(source_lang, target_lang)

    tokenizer = model_data["tokenizer"]
    model = model_data["model"]

    tokens = tokenizer(text, return_tensors="pt", padding=True)

    translated = model.generate(**tokens)

    result = tokenizer.decode(translated[0], skip_special_tokens=True)

    return {
        "source_language": source_lang,
        "translation": result
    }