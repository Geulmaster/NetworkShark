from configparser import ConfigParser

def config_reader():
    parser = ConfigParser()
    parser.read("configuration.ini")
    return parser

def change_config_file(key, value):
    file_content = config_reader()
    file_content.set("CONF", key, value)
    with open("configuration.ini", "w") as config_file:
        file_content.write(config_file)
