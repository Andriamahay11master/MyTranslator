from app.models.translator_model import TranslatorModel

# Example model
model = TranslatorModel("Helsinki-NLP/opus-mt-en-fr")

def translate_text(text: str):
    return model.translate(text)