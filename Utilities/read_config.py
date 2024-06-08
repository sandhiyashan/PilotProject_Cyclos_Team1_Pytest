from configparser import ConfigParser

def get_config(category, key):
    config = ConfigParser()
    config.read("C:\\cyclos_Pytest_project\\PilotProject_Cyclos_Team1_Pytest-2\\Configurations\\config.ini")
    return config.get(category, key)
