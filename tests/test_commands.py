import sys
sys.path.append(".")

import unittest
import os

import pmge.interpreter.command_interpreter

class CommandTest(unittest.TestCase):

    def test_handleCommand(self):
        interpreter = pmge.interpreter.command_interpreter.CommandInterpreter()

if __name__ == '__main__':
    unittest.main()