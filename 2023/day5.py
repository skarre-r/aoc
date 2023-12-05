"""
TODO.
"""

from __future__ import annotations


def process_input() -> ...:
    with open(file="day5.txt", mode="r", newline="\n") as input_file:
        lines: list[str] = [l for line in input_file.readlines() if (l := line.strip())]
    seeds: list[int] = [int(seed) for seed in (lines[0].split(":")[1]).split(" ") if seed]

    maps: list[...] = []

    return seeds, maps


def solve_part_1(seeds: list[int], maps: list[...]) -> ...:
    ...


def solve_part_2(seeds: list[int], maps: list[...]) -> ...:
    ...


def main() -> None:
    seeds, maps = process_input()
    part_1_answer = solve_part_1(seeds, maps)
    print(f"{part_1_answer=}")
    part_2_answer = solve_part_2(seeds, maps)
    print(f"{part_2_answer=}")


if __name__ == "__main__":
    main()
