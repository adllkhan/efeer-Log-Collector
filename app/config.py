# Base Config
host = "0.0.0.0"
port = 8000
origins = ["0.0.0.0"]


# Wazuh Config
class Wazuh:
    alerts_dir = "/var/ossec/logs/alerts"
