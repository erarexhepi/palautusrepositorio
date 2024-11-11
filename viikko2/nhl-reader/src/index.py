from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.console import Console
from rich.table import Table


def main():
    console = Console ()

    season = console.input("Select season (example 2018-19):").strip()
    nationality = console.input("Select nationality (example FIN):").strip().upper()

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)

    table = Table(title=f"Top scorers of {nationality} season {season}")

    table.add_column("Name", justify="left", style="green", no_wrap=True)
    table.add_column("Team", justify="center", style="red")
    table.add_column("Goals", justify="right", style="yellow")
    table.add_column("Assists", justify="right", style="yellow")
    table.add_column("Points", justify="right", style="yellow")

    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points))
    
    console.print(table)
if __name__ == "__main__":
    main()


    
