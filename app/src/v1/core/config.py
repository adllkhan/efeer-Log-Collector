import os
import yaml


dir = os.getcwd()
with open(f"{dir}/app/settings.yaml", "rt") as file:
    settings = yaml.safe_load(file.read())


class Wazuh:
    alerts_dir = settings["wazuh"]["alerts_dir"]
