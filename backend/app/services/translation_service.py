from app.models.model_manager import ModelManager
from app.utils.language_utils import detect_language
from app.utils.text_utils import split_text

model_manager = ModelManager()

def translate_text(text, target_lang):

    source_lang = detect_language(text)

    model_data = model_manager.get_model(source_lang, target_lang)

    tokenizer = model_data["tokenizer"]
    model = model_data["model"]

    chunks = split_text(text)

    translated_chunks = []

    for chunk in chunks:

        tokens = tokenizer(chunk, return_tensors="pt", padding=True)

        translated = model.generate(**tokens)

        result = tokenizer.decode(translated[0], skip_special_tokens=True)

        translated_chunks.append(result)

    final_translation = " ".join(translated_chunks)

    return {
        "source_language": source_lang,
        "translation": final_translation
    }