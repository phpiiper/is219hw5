from abc import ABC, abstractmethod
import multiprocessing
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}
    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command
    def execute_command(self, command_name: str):
        try:
            # self.commands[command_name].execute()
            process = multiprocessing.Process(target=self.commands[command_name].execute())
            process.start()
            process.join()
        except KeyError:
            print(f"No such command: {command_name}")
