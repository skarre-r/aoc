"""
Part 1:
Figure out which games (lines) are valid.
A game is valid as long as none of the red/ green/ values exceed their max.
The answer is the sum of all the valid game IDs.

Part 2:
In each game, find the highest red/ green/ blue values and multiply them together.
The answer is the sum of all those values..
"""

from __future__ import annotations

from typing import Final, TypeAlias

MAX_RED: Final[int] = 12
MAX_GREEN: Final[int] = 13
MAX_BLUE: Final[int] = 14

Play: TypeAlias = dict[str, int]
Game: TypeAlias = list[Play]


def process_input() -> list[Game]:
    with open(file="day2.txt", mode="r", newline="\n") as input_file:
        lines: list[str] = [x for y in input_file.readlines() if (x := y.strip())]
    games: list[Game] = []
    for line in lines:
        game: Game = []
        for cubes in [x for y in (line.split(":")[1]).split(";") if (x := y.strip())]:
            game.append(
                {value[1]: int(value[0]) for value in [cube.strip().split(" ") for cube in cubes.split(",")] if value}
            )
        games.append(game)
    return games


def solve_part_1(games: list[Game]) -> int:
    valid_game_ids: list[int] = []
    for index, game in enumerate(games):
        if not (
                any([play["red"] > MAX_RED for play in game if "red" in play])
                or any([play["green"] > MAX_GREEN for play in game if "green" in play])
                or any([play["blue"] > MAX_BLUE for play in game if "blue" in play])
        ):
            valid_game_ids.append((index + 1))
    return sum(valid_game_ids)


def solve_part_2(games: list[Game]) -> int:
    rgb_power: list[int] = []
    for game in games:
        red: int = max([play.get("red", 0) for play in game])
        green: int = max([play.get("green", 0) for play in game])
        blue: int = max([play.get("blue", 0) for play in game])
        rgb_power.append(red * green * blue)
    return sum(rgb_power)


def main():
    games: list[Game] = process_input()
    part_1_answer = solve_part_1(games=games)
    print(f"{part_1_answer=}")
    part_2_answer = solve_part_2(games=games)
    print(f"{part_2_answer=}")


if __name__ == '__main__':
    main()
