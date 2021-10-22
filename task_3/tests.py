import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_determine_next_action(self):
        self.assertEqual(logic.determine_next_action(), 4, "Should be from 1 to 4")