from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    print("Pelaajat, joilla on vähintään 5 maalia, vähintään 20 syöttöä ja jotka pelaavat PHI-joukkueessa:")
    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(20, "assists"),
        PlaysIn("PHI")
    )

    for player in stats.matches(matcher):
        print(player)

    print("\nKaikki pelaajat (All):")
    all_players = stats.matches(All())
    print(f"Kokonaismäärä: {len(all_players)} pelaajaa")

    print("\nNYR-pelaajat, joilla on alle 2 maalia (Not + HasAtLeast):")
    matcher = And(
        Not(HasAtLeast(2, "goals")),
        PlaysIn("NYR")
    )
    for player in stats.matches(matcher):
        print(player)

    print("\nPelaajat, joilla on alle 5 maalia (HasFewerThan):")
    matcher = HasFewerThan(5, "goals")
    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
