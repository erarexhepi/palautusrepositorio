import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_player_found(self):
        player = self.stats.search("Lemieux")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Lemieux")

    def test_search_player_not_found(self):
        player = self.stats.search("NonExistent")
        self.assertIsNone(player)

    def test_team(self):
        team_players = self.stats.team("EDM")
        self.assertEqual(len(team_players), 3)
        self.assertTrue(all(player.team == "EDM" for player in team_players))

    def test_team_no_players(self):
        team_players = self.stats.team("NonExistentTeam")
        self.assertEqual(len(team_players), 0)

    def test_top_points(self):
        top_players = self.stats.top(3, SortBy.POINTS)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")
        self.assertEqual(top_players[2].name, "Yzerman")

    def test_top_goals(self):
        top_players = self.stats.top(3, SortBy.GOALS)
        self.assertEqual(top_players[0].name, "Lemieux")
        self.assertEqual(top_players[1].name, "Yzerman")
        self.assertEqual(top_players[2].name, "Kurri")

    def test_top_assists(self):
        top_players = self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual(top_players[0].name, "Gretzky")  # Eniten syöttöjä
        self.assertEqual(top_players[1].name, "Yzerman")  # Toiseksi eniten syöttöjä
        self.assertEqual(top_players[2].name, "Lemieux")  # Kolmanneksi eniten syöttöjä


if __name__ == "__main__":
    unittest.main()
