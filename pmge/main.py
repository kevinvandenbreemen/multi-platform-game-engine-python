from command_interpreter import CommandInterpreter
import default_commands

print("Trying to import shit")

interpreter = CommandInterpreter()
interpreter.addCommand(default_commands.About())
interpreter.handle('test')
interpreter.handle("ABOUT me")