from transformers import MarianMTModel, MarianTokenizer

class TranslatorModel:
    
    def __init__(self, model_name):
        self.model_name = model_name
        self.tokenizer = MarianTokenizer.from_pretrained(model_name)
        self.model = MarianMTModel.from_pretrained(model_name)

    def translate(self, text):
        tokens = self.tokenizer(text, return_tensors="pt", padding=True)
        translated = self.model.generate(**tokens)
        result = self.tokenizer.decode(translated[0], skip_special_tokens=True)
        return result