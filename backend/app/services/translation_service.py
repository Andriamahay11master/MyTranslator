from app.models.model_manager import ModelManager

model_manager = ModelManager()

def translate_text(text, source_lang, target_lang):

    model_data = model_manager.get_model(source_lang, target_lang)

    tokenizer = model_data["tokenizer"]
    model = model_data["model"]

    tokens = tokenizer(text, return_tensors="pt", padding=True)

    translated = model.generate(**tokens)

    result = tokenizer.decode(translated[0], skip_special_tokens=True)

    return result