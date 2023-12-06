"""
TODO.
"""

from __future__ import annotations


def process_input() -> ...:
    with open(file="day6.txt", mode="r", newline="\n") as input_file:
        lines: list[str] = [line for _line in input_file.readlines() if (line := _line.strip())]
    ...


def solve_part_1() -> int:
    ...


def solve_part_2() -> int:
    ...


def main() -> None:
    part_1_answer: int = solve_part_1()
    print(f"{part_1_answer=}")
    part_2_answer: int = solve_part_2()
    print(f"{part_2_answer=}")


if __name__ == "__main__":
    main()
