import unittest
from UDPServer.message_parser import MessageParser


class MyTestCase(unittest.TestCase):
    def test_correct_message(self):
        parser = MessageParser()
        parser.parse(b'%cd_000000@')
        self.assertEqual((b'cd', b'000000'), parser.parsed_message)

    def test_correct_message_1(self):
        parser = MessageParser()
        parser.parse(b'%fe_20_40_40_90_FEFEFE@')
        self.assertEqual((b'fe', 20, 40, 40, 90, b'FEFEFE'), parser.parsed_message)

    def test_correct_message_2(self):
        parser = MessageParser()
        parser.parse(b'%fe_345_40_40_90_FEFEFE@')
        self.assertEqual((b'fe', 345, 40, 40, 90, b'FEFEFE'), parser.parsed_message)

    def test_incorrect_command(self):
        parser = MessageParser()
        parser.parse(b'%rewq_20_40_40_90_FEFEFE@')
        self.assertEqual(None, parser.parsed_message)
        self.assertEqual(True, parser.error)
        self.assertEqual("Command b'rewq' not found", parser.message)

    def test_incorrect_num_arg(self):
        parser = MessageParser()
        parser.parse(b'%fe_3456_40_40_90_FEFEFE@')
        self.assertEqual(None, parser.parsed_message)
        self.assertEqual(True, parser.error)
        self.assertEqual("Bad argument #0 b'3456'", parser.message)

    def test_incorrect_num_of_args(self):
        parser = MessageParser()
        parser.parse(b'%fe_30_40_40_90_53_FEFEFE@')
        self.assertEqual(None, parser.parsed_message)
        self.assertEqual(True, parser.error)
        self.assertEqual("Number of params for command b'fe' must be 5", parser.message)

    def test_incorrect_color_code(self):
        parser = MessageParser()
        parser.parse(b'%fe_345_40_40_90_kjlr32@')
        self.assertEqual(None, parser.parsed_message)
        self.assertEqual(True, parser.error)
        self.assertEqual("Bad argument #4 b'kjlr32'", parser.message)

    def test_incorrect_start_symbol(self):
        parser = MessageParser()
        parser.parse(b'23fe_345_40_40_90_F32F45@')
        self.assertEqual(None, parser.parsed_message)
        self.assertEqual(True, parser.error)
        self.assertEqual("Not found begin or end char", parser.message)

    def test_incorrect_start_symbol_1(self):
        parser = MessageParser()
        parser.parse(b'fe_345_40_40_90_F32F45@')
        self.assertEqual(None, parser.parsed_message)
        self.assertEqual(True, parser.error)
        self.assertEqual("Not found begin or end char", parser.message)

    def test_incorrect_end_symbol(self):
        parser = MessageParser()
        parser.parse(b'%fe_345_40_40_90_F32F45')
        self.assertEqual(None, parser.parsed_message)
        self.assertEqual(True, parser.error)
        self.assertEqual("Not found begin or end char", parser.message)

    def test_incorrect_end_symbol_1(self):
        parser = MessageParser()
        parser.parse(b'%fe_345_40_40_90_F32F45f3t33')
        self.assertEqual(None, parser.parsed_message)
        self.assertEqual(True, parser.error)
        self.assertEqual("Not found begin or end char", parser.message)


if __name__ == '__main__':
    unittest.main()
