from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, Or, HasAtLeast, PlaysIn

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    print("Pelaajat, joilla on vähintään 45 maalia tai 70 syöttöä:")
    matcher = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
    )
    for player in stats.matches(matcher):
        print(player)

    print("\nPelaajat, joilla on vähintään 70 pistettä ja jotka pelaavat NYR-, FLA- tai BOS-joukkueissa:")
    matcher = And(
        HasAtLeast(70, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
        )
    )
    for player in stats.matches(matcher):
        print(player)

if __name__ == "__main__":
    main()
