import unittest
from unittest.mock import patch
import dice

class TestGameDice(unittest.TestCase):
    @patch('dice.game_dice')
    def test_game(self, mock_func):
        self.assertTrue(dice.game_dice is mock_func)

        with patch('builtins.input', return_value='r'):
            dice.game_dice(3, 5)

        self.assertTrue(mock_func.called)

if __name__ == '__main__':
    unittest.main()
