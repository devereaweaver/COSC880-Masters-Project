import configparser
import os

# Point to config file
CONFIG_FILE = "config.cfg"

# Instantiate config manager object
config = configparser.ConfigParser()

# Load config data
config.read(CONFIG_FILE)


# Extract Fred API Key
fred_api_key = config['fred-credentials']['api-key']