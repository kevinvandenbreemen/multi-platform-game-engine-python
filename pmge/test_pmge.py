import unittest
from command_interpreter import CommandInterpreter
from default_commands import About

class CommandTest(unittest.TestCase):

    def test_handleCommand(self):
        interpreter = CommandInterpreter()
        interpreter.handle("no such command")

    def test_indicatesCommandHandledSuccessfully(self):
        interpreter = CommandInterpreter()
        interpreter.addCommand(About())
        self.assertEqual(interpreter.handle("ABOUT"), True)

    def test_indicatesCommandWasNotFound(self):
        interpreter = CommandInterpreter()
        self.assertFalse(interpreter.handle("noSuchCommand"))

if __name__ == '__main__':
    unittest.main()