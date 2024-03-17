import os
import yaml


dir = os.getcwd()
with open(f"{dir}/settings.yaml", "rt") as file:
    settings = yaml.safe_load(file.read())


class Wazuh:
    events_dir = settings["wazuh"]["events_dir"]
