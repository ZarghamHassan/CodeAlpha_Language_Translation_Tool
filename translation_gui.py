# translation_gui.py

import tkinter as tk
from tkinter import ttk, messagebox
from translator import LanguageTranslationTool

class TranslationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translation Tool")
        self.root.geometry("400x300")

        self.translation_tool = LanguageTranslationTool()

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        # Input Text Label
        tk.Label(self.root, text="Enter text to translate:").pack(pady=10)

        # Input Text Area
        self.input_text = tk.Text(self.root, height=5, width=40)
        self.input_text.pack()

        # Language Selection
        tk.Label(self.root, text="Select target language:").pack(pady=10)
        
        self.language_combo = ttk.Combobox(self.root, values=list(self.translation_tool.list_languages().values()), state="readonly")
        self.language_combo.pack()
        self.language_combo.current(0)  # Set default selection

        # Translate Button
        self.translate_button = tk.Button(self.root, text="Translate", command=self.perform_translation)
        self.translate_button.pack(pady=10)

        # Output Text Label
        tk.Label(self.root, text="Translated text:").pack(pady=10)

        # Output Text Area
        self.output_text = tk.Text(self.root, height=5, width=40)
        self.output_text.pack()

    def perform_translation(self):
        """Perform the translation and display the result."""
        text_to_translate = self.input_text.get("1.0", tk.END).strip()
        selected_language = self.language_combo.get()

        # Get language code from the selected language
        lang_code = [code for code, name in self.translation_tool.list_languages().items() if name == selected_language]
        
        if lang_code:
            lang_code = lang_code[0]
        else:
            messagebox.showerror("Error", "Language not found.")
            return

        try:
            translated_text = self.translation_tool.translate_text(text_to_translate, lang_code)
            self.output_text.delete("1.0", tk.END)  # Clear previous output
            self.output_text.insert(tk.END, translated_text)  # Insert translated text
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = TranslationApp(root)
    root.mainloop()
