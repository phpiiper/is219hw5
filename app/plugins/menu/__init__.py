from app.commands import Command
from app import App


class MenuCommand(Command):
    def execute(self):
        app = App()
        commands = app.command_handler.commands
        print(f'-----------------')
        print(f'List of Commands:')
        for command in commands:
            print(" > " + command)
        print(f'-----------------')