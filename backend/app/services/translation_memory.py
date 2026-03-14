translation_memory = {}

def get_from_memory(text, source, target):
    key = f"{source}-{target}-{text}"
    return translation_memory.get(key)


def save_to_memory(text, source, target, translation):
    key = f"{source}-{target}-{text}"
    translation_memory[key] = translation