import os
import yaml


dir = os.getcwd()
with open(f"{dir}/app/settings.yaml", "rt") as file:
    settings = yaml.safe_load(file.read())


class Base:
    host = settings["base"]["host"]
    port = settings["base"]["port"]
    origins = list(settings["base"]["origins"])
    allow_credentials = bool(settings["base"]["allow_credentials"])
    methods = list(settings["base"]["methods"])
    headers = list(settings["base"]["headers"])
