import keyboard
from pathlib import Path
import os
import shutil

PATH = Path.home() / 'Desktop/Ideas'
NEW_FILE = 'NewNote'
EXTENSION = '.txt'
FILE = NEW_FILE + EXTENSION

DEBUG = 'errors.txt'
MUST_DELETE = '\\/*?:<>|\"'

def new_note():
    try:
        open(PATH / FILE, "a+")  # creating
        os.startfile(PATH / FILE)  # ACTUALY opening file
    except:
        pass


def rename_note():
    try:
        with open(PATH / FILE, encoding='utf-8') as f:
            new_name = f.readline()
        new_name = new_name.split('\n')[0]
        for item in MUST_DELETE:
            new_name = new_name.replace(item, "")
        new_name = new_name + EXTENSION
        shutil.move(PATH / FILE, PATH / new_name)
    except Exception as err:
        with open(PATH / ('rename ' + DEBUG), "a+") as errors:
            errors.write(str(err))


def open_dir():
    try:
        os.startfile(PATH)
    except Exception as err:
        with open(PATH / ('open '+ DEBUG), "a+") as errors:
            errors.write(str(err))


keyboard.add_hotkey('ctrl+alt+q', lambda: new_note())
keyboard.add_hotkey('ctrl+alt+w', lambda: open_dir())
keyboard.add_hotkey('ctrl+alt+e', lambda: rename_note())
keyboard.wait()
