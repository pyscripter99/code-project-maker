import os, shutil, re, json
from tkinter import *

config = {}
with open("config.json", "r") as f:
    config = json.load(f)

for k in config.keys():
    config[k] = config[k].replace("%LOGIN%", os.getlogin())

BASE_PATH = config["base_path"]
EDITOR_COMMAND = config["editor_command"]
TEMPLATE = config["template"]

root = Tk()
root.title("Create project")
main_lbl = Label(root, text="Create a new project.")
main_lbl.pack()

pj_name = StringVar()
def pj_callback(var, index, mode):
    pj_name.set(re.sub("[0-9]", '', pj_name.get()))

pj_name.trace_add("write", pj_callback)

pj_name_ent = Entry(root, textvariable=pj_name)
pj_name_ent.pack()
pj_name_ent.focus()

use_template = IntVar()

use_template_check = Checkbutton(root, text="Use template", variable=use_template)
use_template_check.select()
use_template_check.pack()

def close(a=None, b=None, c=None):
    root.destroy()
    exit(1)

def toggle_template(ignore=None):
    if use_template.get() == 1:
        use_template.set(0)
    else:
        use_template.set(1)

def make(ignore=None):
    os.chdir(BASE_PATH)
    if use_template.get() == 0:
        os.mkdir(pj_name.get())
    else:
        shutil.copytree(TEMPLATE, BASE_PATH + pj_name.get())
    os.chdir(pj_name.get())
    os.system(EDITOR_COMMAND)
    close()

create_btn = Button(root, text="Create", command=make)
create_btn.pack()
root.bind("<Return>", make)
root.bind("1", toggle_template)
root.bind("<Escape>", close)

root.mainloop()