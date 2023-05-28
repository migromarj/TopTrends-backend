from googletrans import Translator


def translate_to_english(text):
    if text is None:
        return ""
    else:
        translator = Translator()
        try:
            english = translator.translate(text, dest='en').text
            if english:
                return english
            return ""
        except Exception:
            return text
