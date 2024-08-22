import runpy
import os, sys

now_dir = os.getcwd()
runpy.run_path(now_dir + "\\Inference\\src\\tts_backend.py")
