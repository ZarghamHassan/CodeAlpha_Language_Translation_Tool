# Import necessary libraries
from googletrans import Translator, LANGUAGES

# Define the Translation Tool class
class LanguageTranslationTool:
    def __init__(self):
        self.translator = Translator()

    def list_languages(self):
        """List all available languages for translation."""
        return LANGUAGES

    def translate_text(self, text, dest_language):
        """Translate text to the specified destination language."""
        translated = self.translator.translate(text, dest=dest_language)
        return translated.text

# Main function to run the translation tool
if __name__ == "__main__":
    translation_tool = LanguageTranslationTool()

    # Display available languages
    print("Available languages:")
    for lang_code, lang_name in translation_tool.list_languages().items():
        print(f"{lang_code}: {lang_name}")

    # Get user input for translation
    text_to_translate = input("\nEnter text to translate: ")
    target_language = input("Enter the target language code (e.g., 'fr' for French): ")

    # Perform translation
    try:
        translated_text = translation_tool.translate_text(text_to_translate, target_language)
        print(f"\nTranslated text: {translated_text}")
    except Exception as e:
        print(f"Error: {e}")
