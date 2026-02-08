import unittest
# 制作したファイルを janken.py と仮定してインポート
from main import judge, normalize_input

class TestJanken(unittest.TestCase):

    def test_normalize_input(self):
        """入力の正規化が正しく行われるかテスト"""
        self.assertEqual(normalize_input("1"), "1")
        self.assertEqual(normalize_input("グー"), "1")
        self.assertEqual(normalize_input("チョキ"), "2")
        self.assertEqual(normalize_input("5"), None)  # 不正な入力

    def test_judge_win(self):
        """プレイヤーが勝つパターンのテスト"""
        # 1:グー, 2:チョキ, 3:パー
        self.assertEqual(judge("1", "2"), "win") # グー vs チョキ
        self.assertEqual(judge("2", "3"), "win") # チョキ vs パー
        self.assertEqual(judge("3", "1"), "win") # パー vs グー

    def test_judge_lose(self):
        """プレイヤーが負けるパターンのテスト"""
        self.assertEqual(judge("1", "3"), "lose")
        self.assertEqual(judge("2", "1"), "lose")
        self.assertEqual(judge("3", "2"), "lose")

    def test_judge_draw(self):
        """あいこのパターンのテスト"""
        self.assertEqual(judge("1", "1"), "draw")
        self.assertEqual(judge("2", "2"), "draw")

if __name__ == '__main__':
    unittest.main()
    