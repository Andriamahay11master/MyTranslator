from transformers import MarianMTModel, MarianTokenizer

class ModelManager:

    def __init__(self):
        self.models = {}

    def get_model(self, source_lang, target_lang):

        model_key = f"{source_lang}-{target_lang}"
        model_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"

        if model_key not in self.models:

            tokenizer = MarianTokenizer.from_pretrained(model_name)
            model = MarianMTModel.from_pretrained(model_name)

            self.models[model_key] = {
                "tokenizer": tokenizer,
                "model": model
            }

        return self.models[model_key]