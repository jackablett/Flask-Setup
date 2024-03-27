from termcolor import colored
from click import echo
import shutil
import os

def path(string: str) -> str:
    return string.lower().replace(" ", "-")

def create_directory(name: str) -> None:
    if not os.path.exists(name):
        os.mkdir(name)
        log(f"Created new project under {name}")

def log(text: str) -> None:
    echo(colored(text, 'cyan'))

def copy_tree(source: str, destination: str, project_type: str) -> None:
    remove_directory(destination)
    create_directory(source)
    shutil.copytree(source, destination)
    log(f"Created a new '{project_type}' project at '{destination}'")

def remove_directory(name: str) -> None:
    if os.path.exists(name):
        shutil.rmtree(name)

def create_config(destination: str, port: int = 80, host: str = "0.0.0.0", debug: bool = True, secret_key: str = "random", site_name: str = "Flask Site", project: str = None) -> None:
    if not project == "flask-admin":
        app_folder = os.path.join(destination, "app")
        if secret_key == "random":
            secret_key = """import random, os
                        
SECRET_KEY = os.urandom(random.randint(999, 9999))                     
    """
        else:
            secret_key = f"SECRET_KEY = '{secret_key}'"
        with open(f"{os.path.join(app_folder, "config.py")}", "w") as config:
            config.write(f"""{secret_key}
PORT = {port}
DEBUG = {debug}
HOST = "{host}"

SITE_NAME = "{site_name}" """)
        
def append_after(destination: str, layout: bool = False, project: str = None) -> None:
    app_folder = os.path.join(destination, "app")
    if layout and not project == "flask-admin":
        with open("utils/examples/layout.html") as old_layout:
            with open(os.path.join(app_folder, "templates", "layout.html"), "w", encoding="utf-8") as new_layout:
                new_layout.write(old_layout.read())

        with open("utils/examples/index.html") as old_page:
            with open(os.path.join(app_folder, "templates", "index.html"), "w", encoding="utf-8") as new_page:
                new_page.write(old_page.read())

    if not project == "flask-admin":
        with open("utils/examples/run.py") as old_run:
            with open(os.path.join(destination, "run.py"), "w", encoding="utf-8") as new_run:
                new_run.write(old_run.read())

def install_tailwind(destination: str) -> None:
    shutil.copyfile("utils/examples/package.json", os.path.join(destination, "package.json"))
    os.makedirs(os.path.join(destination, "app", "static"), exist_ok=True)
    os.system(f"cd {destination} && npm i tailwindcss")
    log("Installed tailwindcss")
    os.makedirs(os.path.join(destination, "app", "static", "css"), exist_ok=True)
    os.system(f"cd {destination} && npm i tailwindcss")
    shutil.copyfile("utils/examples/base.css", os.path.join(destination, "app", "static", "css", "base.css"))
    shutil.copyfile("utils/examples/tailwind.config.js", os.path.join(destination, "tailwind.config.js"))
    os.system(f"cd {destination} && npx tailwindcss -i app/static/css/base.css -o app/static/css/styles.css")
    log("Created base.css & styles.css to be used in index.html")