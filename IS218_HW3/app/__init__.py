import pkgutil
import importlib
from app.commands import CommandHandler
from app.commands import Command

class App: 
    def __init__(self):
        self.command_handler = CommandHandler()

    def load_plugins(self):
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.','/')]):
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
        self.load_plugins()
        print("Hello world!, Type 'exit' to exit.")
        while True:
            user_input = input(">>> ").strip()
            if user_input.lower() == 'exit':
                raise SystemExit("Exiting...")
            parts = user_input.split()
            command_name = parts[0]
            args = parts[1:]

            try:
                self.command_handler.execute_command(command_name, *args)
            except Exception as e:
                print(f"Error: {e}")