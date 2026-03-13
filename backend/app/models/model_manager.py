from transformers import MarianMTModel, MarianTokenizer
from app.utils.supported_languages import SUPPORTED_MODELS


class ModelManager:

    def __init__(self):
        self.models = {}

    def get_model(self, source_lang, target_lang):

        model_key = f"{source_lang}-{target_lang}"

        if model_key not in SUPPORTED_MODELS:
            raise ValueError(f"Translation {model_key} not supported")

        if model_key not in self.models:

            model_name = SUPPORTED_MODELS[model_key]

            tokenizer = MarianTokenizer.from_pretrained(model_name)
            model = MarianMTModel.from_pretrained(model_name)

            self.models[model_key] = {
                "tokenizer": tokenizer,
                "model": model
            }

        return self.models[model_key]