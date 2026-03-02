from engine import PlayerPerformance, MatchContext, get_match_ratings

# Quick example for testing
test_players = [
    PlayerPerformance(name="Sitetampo", brawlers="Frank", kills=5, dps=350, won=True)
]
context = MatchContext(map_name="Pinhole Punt", game_mode="Brawl Ball", series_score="2-0")

ratings = get_match_ratings(test_players, context)
print(ratings)
