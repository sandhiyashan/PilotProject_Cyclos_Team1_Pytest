from configparser import ConfigParser

def get_config(category, key):
    config = ConfigParser()
    config.read("E:\PilotProject_Cyclos_Team1_Pytest-1\Configurations\config.ini")
    return config.get(category, key)
