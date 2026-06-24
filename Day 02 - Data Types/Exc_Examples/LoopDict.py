players = {
    "player1": {"name": "Alex", "level": 5},
    "player2": {"name": "Sam", "level": 8},
    "player3": {"name": "Lina", "level": 3}
}

for player_id, player_info in players.items():
    print(f"\n{player_id}:")

    for key, value in player_info.items():
        print(key, value)

