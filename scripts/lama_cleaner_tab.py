import os
import sys

import gradio as gr

from modules import scripts, script_callbacks, sd_models, shared

import launch

dir = os.path.dirname(os.path.dirname(__file__))

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

def set_start_command(command):
    with open(dir + '/start_cmd.txt', 'w', encoding='utf-8') as f:
        f.write(command)

def set_open_command(command):
    with open(dir + '/open_cmd.txt', 'w', encoding='utf-8') as f:
        f.write(command)

def get_start_command():
    if os.path.exists(dir + '/start_cmd.txt'):
        with open(dir + '/start_cmd.txt', 'r', encoding='utf-8') as f:
            command = f.read()
        print(command)
    elif os.name == 'nt':
        command = 'start venv/Scripts/lama-cleaner --model=lama --device=cpu --port=7870'
    else: # posix
        command = 'venv/bin/lama-cleaner --model=lama --device=cpu --port=7870'

    return command

def get_open_command():
    if os.path.exists(dir + '/open_cmd.txt'):
        with open(dir + '/open_cmd.txt', 'r', encoding='utf-8') as f:
            command = f.read()
    elif os.name == 'nt':
        command = 'start http://127.0.0.1:7870/'
    else: # posix
        command = 'http://127.0.0.1:7870/'
        
    return command

def on_ui_tabs():

    with gr.Blocks() as lama_cleaner_tab:
        status = gr.HTML()
        install = gr.Button("Install / Update")
        start = gr.Button("Start")
        start_command = gr.Textbox(get_start_command(), label="Start Command")
        iframe_height = gr.Textbox(800, label="iframe Height")
        open_iframe = gr.Button("Open")
        open_newtab = gr.Button("Open New Window")
        open_command = gr.Textbox(get_open_command(), label="Open NewTab Command")
        iframe = gr.HTML()

        start_command.change(
            fn=set_start_command,
            inputs=[start_command],
        )

        open_command.change(
            fn=set_open_command,
            inputs=[open_command],
        )

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
