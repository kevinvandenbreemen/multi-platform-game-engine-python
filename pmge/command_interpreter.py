from default_commands import CommandInterface
from default_commands import About

class CommandInterpreter:

    _supportedCommands = []

    def handle(self, command):

        commandName = command.split(None, 1)[0].strip()
        argsLst = command.split(None, 2)
        args = ""
        if len(argsLst) > 1:
            args = argsLst[1]
        
        flt = lambda cmd: cmd.getName() == commandName
        result = list(filter(flt, self._supportedCommands))
        if not result:
            print(f"No command {commandName} exists...")
        else:
            result[0].handle(args)
            return True

        return False

    def addCommand(self, commandInstance):
        if issubclass(type(commandInstance), CommandInterface):
            self._supportedCommands.append(commandInstance)
        else:
            print(f"{type(commandInstance)} is not a command.  Please implement the {CommandInterface} to mark it a command")

if __name__ == '__main__':
    
    interpreter = CommandInterpreter()
    interpreter.addCommand(About())
    interpreter.handle('test')
    interpreter.handle("ABOUT me")