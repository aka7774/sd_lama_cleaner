import os
import sys

import gradio as gr

from modules import scripts, script_callbacks, sd_models, shared

import launch

def install_lama_cleaner():
    try:
        if not launch.is_installed("lama-cleaner"):
            launch.run_pip("install lama-cleaner", desc='lama-cleaner')
    except:
        print("Install failed.")

def start_lama_server():
    lama_path = os.path.abspath(os.path.join('extensions', 'sd_lama_cleaner', 'scripts', 'lama_cleaner_lama.py'))
    command = f"start {sys.executable} {lama_path}"
    launch.run(command)

def open_lama_cleaner(height):
    return f'<iframe src="http://127.0.0.1:7870/" width="100%" height="{height}">'

def start_lama_cleaner():
    command = 'start http://127.0.0.1:7870/'
    launch.run(command)

def on_ui_tabs():
    with gr.Blocks() as lama_cleaner_tab:
        install = gr.Button("Install")
        start = gr.Button("Start")
        iframe_height = gr.Textbox(800, label="iframe Height")
        open_iframe = gr.Button("Open")
        open_newtab = gr.Button("Open New Window")
        iframe = gr.HTML()

        install.click(
            fn=install_lama_cleaner,
        )

        start.click(
            fn=start_lama_server,
        )

        open_iframe.click(
            fn=open_lama_cleaner,
            inputs=[iframe_height],
            outputs=[iframe],
        )

        open_newtab.click(
            fn=start_lama_cleaner,
        )
    
    return (lama_cleaner_tab, "LamaCleaner", "lama_cleaner_tab"),


script_callbacks.on_ui_tabs(on_ui_tabs)
