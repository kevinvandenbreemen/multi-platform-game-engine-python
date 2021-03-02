from command_interpreter import CommandInterpreter
from command_interpreter import CommandInterface

@CommandInterface.register
class About:
    def handle(self, command):
        print(f'I AM THE ABOUT COMMAND! - {command}')

    def getName(self):
        return "ABOUT"

if __name__ == '__main__':
    command = About()
    print(command.getName())
    command.handle('me')
    print(issubclass(About, CommandInterface))
    print(type(command))
    print(issubclass(type(command), CommandInterface))