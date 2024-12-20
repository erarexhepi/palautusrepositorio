from statistics import Statistics
from player_reader import PlayerReader
from query_builder import QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query1 = QueryBuilder()
    m1 = (
        query1
        .plays_in("PHI")
        .has_at_least(10, "assists")
        .has_fewer_than(10, "goals")
        .build()
    )

    query2 = QueryBuilder()
    m2 = (
        query2
        .plays_in("EDM")
        .has_at_least(50, "points")
        .build()
    )

    query3 = QueryBuilder()
    matcher = query3.one_of(m1, m2).build()

    print("Pelaajat, jotka täyttävät ehdon:")
    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
