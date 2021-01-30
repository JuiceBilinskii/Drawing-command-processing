import unittest
from message_parser import MessageParser


class MyTestCase(unittest.TestCase):

    def test_incorrect_colour(self):
        parser = MessageParser()
        parser.message = '%cd_#F81F@%de_20_30_90_105_#07FF@%dr_20_30_90_105_#07FF@'
        self.assertEqual(parser.parse(), False)

    def test_correct_command(self):
        parser = MessageParser()
        parser.message = '%dp_20_30_000000@%de_20_30_90_105_AAE2C2@%dr_20_30_90_105_1AE2C2@'
        self.assertEqual(parser.parse(), [['dp', 20, 30, '000000'], ['de', 20, 30, 90, 105, 'AAE2C2'],
                                          ['dr', 20, 30, 90, 105, '1AE2C2']])

    def test_incorrect_num_attribute(self):
        parser = MessageParser()
        parser.message = '%dp_3a_30_000000@%de_20_30_8l_105_AAE2C2@%dr_20_30_90_105_1AE2C2@'
        self.assertEqual(parser.parse(), False)

    def test_oversize_num_attribute(self):
        parser = MessageParser()
        parser.message = '%dp_2340_30_000000@%de_20_30_90_105_AAE2C2@%dr_20_30_90_105_1AE2C2@'
        self.assertEqual(parser.parse(), False)

    def test_incorrect_num_of_attributes(self):
        parser = MessageParser()
        parser.message = '%dp_20_30_000000@%de_20_30_105_AAE2C2@%dr_20_30_90_105_1AE2C2@'
        self.assertEqual(parser.parse(), False)

    def test_irregular_order_of_attributes(self):
        parser = MessageParser()
        parser.message = '%dp_20_30_000000@%de_20_30_90_AAE2C2_105@%dr_20_30_90_105_1AE2C2@'
        self.assertEqual(parser.parse(), False)


if __name__ == '__main__':
    unittest.main()
