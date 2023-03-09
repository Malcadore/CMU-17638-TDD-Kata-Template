import unittest
from bowling import Bowling

class Testing(unittest.TestCase):
    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)

    def test_bowler(self):
        GAME = Bowling()
        BOWLER1_NAME = 'Travis'
        BOWLER1_ID = GAME.set_bowler(BOWLER1_NAME)
        actual = GAME.get_bowler(BOWLER1_ID)
        self.assertEqual(BOWLER1_NAME, actual)

if __name__ == '__main__':
    unittest.main()
