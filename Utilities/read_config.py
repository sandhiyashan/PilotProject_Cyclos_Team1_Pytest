from configparser import ConfigParser

def get_config(category, key):
    config = ConfigParser()
<<<<<<< Updated upstream
    config.read("/Configurations/config.ini")
=======
    config.read("C:\\cyclos_Pytest_project\\PilotProject_Cyclos_Team1_Pytest-1\\Configurations\\config.ini")
>>>>>>> Stashed changes
    return config.get(category, key)
