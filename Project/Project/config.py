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

# Extract database credentials
db_user = config["database-credentials"]["user"]
db_password = config["database-credentials"]["password"]
db_host = config["database-credentials"]["host"]
db_port = config["database-credentials"]["port"]
db_name = config["database-credentials"]["dbname"]
