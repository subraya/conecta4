
def validate_player_exists(player: str, repository):
    if not repository.get_one_by_key(player):
        return False
    return True