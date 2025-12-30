import unittest
from unittest import TestCase

from other.logger_demo import LoggerManager, ConsolePattern, FilePattern


class TestLoggerManager(TestCase):
    def test_get_logger_console(self):
        self.assertIsNotNone(LoggerManager().get_logger("console"))
        self.assertIsInstance(LoggerManager().get_logger("console").pattern, ConsolePattern)

    def test_get_logger_file(self):
        self.assertIsNotNone(LoggerManager().get_logger("file"))
        self.assertIsInstance(LoggerManager().get_logger("file").pattern, FilePattern)


if __name__ == '__main__':
    unittest.main()