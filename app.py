import re
import jieba
from PIL import Image
from wordcloud import WordCloud
import gradio as gr
from typing import List


def tokenize_text(text:str) -> List:
    """
    
    Tokenize the text by utilising the regex, and then segment the text by jieba.
    Args:
        text: a string mixed with chinese and english.
    Returns:
        a list of tokens.
    """
    compiler = re.findall(r'[\u4e00-\u9fa5]+|[a-zA-Z0-9]+',text)
    
    segmented = []
    for token in compiler:
        if re.match(r'[\u4e00-\u9fa5]', token):
            segmented += jieba.cut(token)
        else:
            segmented.append(token.lower())
            
    return segmented


def generate_world_cloud(text:str) -> Image.Image:
    """
    
    Generate a world cloud from the text.
    Args:
        text: a string mixed with chinese and english.
    Returns:
        Image: PIL.Image.Image
    """
    
    segmented = tokenize_text(text)
    
    wc = WordCloud(
        font_path="simhei.ttf", 
        width=800,
        height=400,
        background_color='white'
    )
    
    return wc.generate(" ".join(segmented)).to_image()   

def generate_word_cloud_from_file(file:str) -> Image.Image:
    """
    Generate a word cloud from a file.
    Args:
        file: a file path.
    Returns:
        Image: PIL.Image.Image
    """
    text = open(file, "r", encoding="utf-8").read()
    return generate_world_cloud(text)
   
with gr.Blocks(title="World Cloud Generator") as demo:
    gr.Markdown("## Word Cloud Generator\nSupports mixed Chinese-English input via **text** or **.txt file upload**.")
    with gr.Tab("Text Input"):
        with gr.Row():
            text_input = gr.Textbox(lines=10, label="Input texts")
        text_button = gr.Button("Generate Word Cloud")
        text_output = gr.Image(type="pil", label="world cloud")
        text_button.click(generate_world_cloud, inputs=text_input, outputs=text_output)
    with gr.Tab("File Input"):
        with gr.Row():
            file_input = gr.File(label="Upload .txt file")
        file_button = gr.Button("Generate Word Cloud")
        file_output = gr.Image(type="pil", label="world cloud")
        file_button.click(generate_word_cloud_from_file, inputs=file_input, outputs=file_output)
        

demo.launch()
