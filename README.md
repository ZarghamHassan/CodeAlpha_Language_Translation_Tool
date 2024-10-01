# Language Translation Tool

This is a simple language translation tool that uses Google Translate API for translating text from one language to another. It has a graphical user interface (GUI) built using `tkinter` and a separate file for handling the translation logic.

## Project Structure

- `translator.py`: This file contains the `LanguageTranslationTool` class, which handles text translation using the `googletrans` library.
- `translation_gui.py`: This file builds the GUI using `tkinter`, allowing users to enter text, select the target language, and display the translated text.

## Prerequisites

- Python 3.x
- `googletrans` library (Google Translate API wrapper)
- `tkinter` (usually comes pre-installed with Python)

### Installing `googletrans`

You can install the `googletrans` library by running:

```bash
pip install googletrans==4.0.0-rc1
```
## How to Run
1. Clone or download the repository.

2. Make sure you have Python 3.x installed and the googletrans library set up.

3. Navigate to the language_translation_tool directory.

4.  the GUI using the following command:
```bash
python translation_gui.py
```
## Features
- **Text Input**: Enter the text you want to translate.
- **Language Selection**: Choose the target language from the dropdown list.
- **Translation**: Click the "Translate" button to get the translated text.
## Example Usage
1. Enter some text in the "Enter text to Translate" Box
2. Select the language to which you want the text to be translated from the dropdown.
3. Click the "Translate" button to view the translated text in the output area.
