# Configuration settings for Chess Game Backend

DATABASE_SETTINGS = {
    'host': 'localhost',
    'port': 5432,
    'user': 'chess_user',
    'password': 'secure_password',
    'database': 'chess_db'
}

AI_PARAMETERS = {
    'difficulty': 'medium',
    'evaluation_function': 'basic_evaluation',
    'search_depth': 3
}

GAME_RULES = {
    'time_control': '30+10', # 30 minutes plus 10 seconds increment
    'max_games': 10,
    'board_size': 8
}