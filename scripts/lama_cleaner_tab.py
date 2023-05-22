import os
import sys

import gradio as gr

from modules import scripts, script_callbacks, sd_models, shared

import launch

def install_lama_cleaner():
    try:
        launch.run_pip("install -U lama-cleaner", desc='lama-cleaner')
        return ['Installed.']
    except:
        print("Install failed.")

def start_lama_server(command):
    launch.run(command)
    return ['Server started.']

def open_lama_cleaner(height):
    return f'<iframe src="http://127.0.0.1:7870/" width="100%" height="{height}">'

def start_lama_cleaner(command):
    launch.run(command)

def on_ui_tabs():
    with gr.Blocks() as lama_cleaner_tab:
        status = gr.HTML()
        install = gr.Button("Install / Update")
        start = gr.Button("Start")
        start_command = gr.Textbox('start venv/Scripts/lama-cleaner --model=lama --device=cpu --port=7870', label="Start Command")
        iframe_height = gr.Textbox(800, label="iframe Height")
        open_iframe = gr.Button("Open")
        open_newtab = gr.Button("Open New Window")
        open_command = gr.Textbox('start http://127.0.0.1:7870/', label="Open NewTab Command")
        iframe = gr.HTML()

        install.click(
            fn=install_lama_cleaner,
            outputs=[status],
        )

        start.click(
            fn=start_lama_server,
            inputs=[start_command],
            outputs=[status],
        )

        open_iframe.click(
            fn=open_lama_cleaner,
            inputs=[iframe_height],
            outputs=[iframe],
        )

        open_newtab.click(
            fn=start_lama_cleaner,
            inputs=[open_command],
        )
    
    return (lama_cleaner_tab, "LamaCleaner", "lama_cleaner_tab"),


script_callbacks.on_ui_tabs(on_ui_tabs)
