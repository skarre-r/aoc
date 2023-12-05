"""
Part 1:
Figure out which games (lines) are valid.
A game is valid as longs as none of the red/ green/ value values exceed their max.
The answer is the sum of all the valid game IDs.

Part 2:
...
"""

from __future__ import annotations

from typing import TypedDict, Final, TypeAlias

MAX_RED: Final[int] = 12
MAX_GREEN: Final[int] = 13
MAX_BLUE: Final[int] = 14


class Play(TypedDict):
    red: int
    green: int
    blue: int


Game: TypeAlias = list[Play]


# TODO handle double digit values
def process_input() -> list[Game]:
    """I dislike working with strings."""
    with open(file="day2.txt", mode="r", newline="\n") as input_file:
        lines: list[str] = [line for input_file_line in input_file.readlines() if (line := input_file_line.strip())]
    games: list[list[Play]] = []

    # TODO improve
    for line in lines:
        _, all_plays = line.split(":")  # type: str, str
        processed_plays: list[Play] = []
        for individual_play in [y for x in all_plays.split(";") if (y := x.strip())]:
            processed_play: Play = {
                "red": 0,
                "green": 0,
                "blue": 0
            }
            for color_value in [x for y in individual_play.split(",") if (x := y.strip())]:
                value: int = int(color_value[0])
                for key in processed_play.keys():
                    if key in color_value:
                        processed_play[key] = value
                        break
            processed_plays.append(processed_play)
        games.append(processed_plays)
    return games


def solve_part_1(games: list[Game]) -> int:
    valid_game_ids: list[int] = []
    for index, game in enumerate(games):
        if not (
                any([play["red"] > MAX_RED for play in game])
                and any([play["green"] > MAX_GREEN for play in game])
                and any([play["blue"] > MAX_BLUE for play in game])
        ):
            valid_game_ids.append((index + 1))

    return sum(valid_game_ids)


def solve_part_2(games: list[Game]) -> int:
    ...


def main():
    games: list[Game] = process_input()
    part_1_answer = solve_part_1(games=games)
    print(f"{part_1_answer=}")
    part_2_answer = solve_part_2(games=games)
    print(f"{part_2_answer=}")


if __name__ == '__main__':
    main()
