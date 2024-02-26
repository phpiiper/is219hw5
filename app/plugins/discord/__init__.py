from app.commands import Command


class DiscordCommand(Command):
    def execute(self):
        print(f'I WILL send something to discord')