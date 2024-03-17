import os
import yaml


dir = os.getcwd()
with open(f"{dir}/settings.yaml", "rt") as file:
    settings = yaml.safe_load(file.read())


class Config:
    host = settings["base"]["host"]
    port = settings["base"]["port"]

    class Cors:
        dashboard_host = settings["cors"]["dashboard_host"]
        allow_credentials = bool(settings["cors"]["allow_credentials"])
        methods = list(settings["cors"]["methods"])
        headers = list(settings["cors"]["headers"])
