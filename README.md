# word_cloud

## Desciption

This is a simple web application that generates word clouds from mixed Chinese-English text. It supports both direct text input and `.txt` file upload. Chinese word segmentation is handled by `jieba`, and the visualization is generated using `WordCloud`.

Demo website: https://huggingface.co/spaces/pandalow/word_cloud_generator

### Features

* Supports both Chinese and English text
* Handles mixed-language input
* Two modes of input:

  * Textbox input
  * `.txt` file upload
* Built with Gradio interface for easy interaction

### Demo

Launch the app with:

```bash
python app.py
```

You will see two tabs:

1. **Text Input** – Paste or type your text.
2. **File Upload** – Upload a UTF-8 encoded `.txt` file.

The app will generate a word cloud image based on the frequency of words.

### Requirements

Install the dependencies:

```bash
pip install jieba wordcloud gradio
```

You will also need to have a Chinese font (e.g., `simhei.ttf`) available in your working directory for proper rendering of Chinese characters.

### Notes

* The uploaded `.txt` file **must be UTF-8 encoded**.
* Emojis and other non-text symbols are ignored during tokenization.

### File Structure

```
.
├── app.py          # Main application file
├── simhei.ttf      # Chinese font required by WordCloud
└── README.md
```

### License

This project is released under the MIT License.