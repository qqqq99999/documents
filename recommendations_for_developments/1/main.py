import random

# --- 純粋関数 (副作用なし) ---

def get_computer_hand():
    """コンピュータの手をランダムに決定する"""
    return random.choice(['1', '2', '3'])

def normalize_input(user_input):
    """ユーザーの入力を内部管理用の '1', '2', '3' に変換する"""
    mapping = {
        '1': '1', '2': '2', '3': '3',
        'グー': '1', 'チョキ': '2', 'パー': '3'
    }
    return mapping.get(user_input)

def judge(player_hand, computer_hand):
    """
    勝敗を判定する純粋なロジック
    戻り値: 'win', 'lose', 'draw'
    """
    # 1:グー, 2:チョキ, 3:パー
    # (自分 - 相手 + 3) % 3  => 0:あいこ, 1:負け, 2:勝ち
    p = int(player_hand)
    c = int(computer_hand)
    result_map = {0: 'draw', 1: 'lose', 2: 'win'}
    return result_map[(p - c + 3) % 3]

def update_stats(stats, result):
    """
    現在の戦績を元に、新しい戦績を返す (不変性を意識)
    """
    new_stats = stats.copy()
    new_stats[result] += 1
    return new_stats

# --- 副作用を伴う関数 (入出力) ---

def get_user_input():
    """ユーザーから有効な入力を受け取るまで繰り返す"""
    prompt = "じゃんけん！ (1:グー, 2:チョキ, 3:パー) > "
    u_input = input(prompt).strip()
    normalized = normalize_input(u_input)
    
    if normalized:
        return normalized
    print("不正な入力です。1, 2, 3 または グー, チョキ, パーで入力してください。")
    return get_user_input() # 再帰呼び出し

def play_round(stats):
    """1回分のゲームを実行し、更新された戦績を返す"""
    hand_names = {'1': 'グー', '2': 'チョキ', '3': 'パー'}
    
    player = get_user_input()
    computer = get_computer_hand()
    
    result = judge(player, computer)
    
    print(f"\nあなた: {hand_names[player]} vs コンピュータ: {hand_names[computer]}")
    print(f"結果: {result.upper()}!")
    
    return update_stats(stats, result)

def main():
    """メインループ（再帰ではなくwhileで実用的に実装）"""
    current_stats = {'win': 0, 'lose': 0, 'draw': 0}
    
    print("--- じゃんけんゲーム開始！ ---")
    
    while True:
        current_stats = play_round(current_stats)
        
        retry = input("\nもう一度遊びますか？ (y/n) > ").lower()
        if retry != 'y':
            break
            
    print("\n--- 最終戦績 ---")
    print(f"{current_stats['win']}勝 {current_stats['lose']}敗 {current_stats['draw']}引き分け")
    print("お疲れ様でした！")

if __name__ == "__main__":
    main()
