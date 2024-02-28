import os
import pkgutil
import importlib
from app.commands import CommandHandler
from app.commands import Command
from dotenv import load_dotenv

class App:
    def __init__(self): # Constructor
        load_dotenv()
        self.settings = {}
        for key,value in os.environ.items():
            self.settings[key] = value
        self.settings.setdefault("ENVIRONMENT","TESTING")
        self.command_handler = CommandHandler()
        self.load_plugins()
    def get_environment_variable(self, env_var: str = "ENVIRONMENT"):
        return self.settings[env_var]
    def load_plugins(self):
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue
    def start(self):
        print("Type 'exit' to exit.")
        while True:
            inp = input(">>> ")
            if (len(inp.split(" ")) > 1):
                split = inp.split(" ")
                self.command_handler.execute_command(split[0],split[1:])
            else:
                self.command_handler.execute_command(inp.strip())
