import os
import json


logs_dir = os.environ.get("LOGS_DIR")


def get_logs_from_wazuh():
    os.chdir(logs_dir)
    with open("alerts.json", "r") as logs:
        return logs.read()


def get_log_from_wazuh(log_id: float):
    os.chdir(logs_dir)
    with open("alerts.json", "r") as logs:
        output = json.load(logs)
        return output
