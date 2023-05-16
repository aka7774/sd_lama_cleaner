from typing import List
from pydantic import BaseModel
from lama_cleaner.server import main

class FakeArgs(BaseModel):
    host: str = "0.0.0.0"
    port: int = 7870
    model: str = 'lama'
    hf_access_token: str = ""
    sd_disable_nsfw: bool = False
    sd_cpu_textencoder: bool = True
    sd_run_local: bool = False
    sd_enable_xformers: bool = False
    local_files_only: bool = False
    cpu_offload: bool = False
    device: str = "cpu"
    gui: bool = False
    gui_size: List[int] = [1000, 1000]
    input: str = ''
    disable_model_switch: bool = True
    debug: bool = False
    no_half: bool = False
    disable_nsfw: bool = False
    enable_xformers: bool = False
    model_dir: str = None
    output_dir: str = None
    enable_interactive_seg: bool = True
    enable_remove_bg: bool = True
    enable_realesrgan: bool = True

if __name__ == "__main__":
    main(FakeArgs())
