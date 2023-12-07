"""
Part 1:
Every number with a special character adjacent to it (incl. diagonals & prev/ next lines) is valid.
the answer is the sum of all the valid numbers.

Part 2:
Like part 1, but every pair of numbers that share an adjacent "*" character must be multiplied together.
"""

from __future__ import annotations

from typing import TypeAlias

PartNumber: TypeAlias = tuple[int, int, int]
PartNumbers: TypeAlias = list[PartNumber]
SpecialCharacters: TypeAlias = list[int]

PartialSchematic: TypeAlias = tuple[SpecialCharacters, PartNumbers]
Schematic: TypeAlias = list[PartialSchematic]


def solve_part_1() -> int:
    with open(file="day3.txt", mode="r", newline="\n") as input_file:
        lines: list[str] = [line for _line in input_file.readlines() if (line := _line.strip())]

    schematic: Schematic = []

    for line in [x for y in lines if (x := y.strip())]:
        wip_index: int | None = None
        special_character_indexes: SpecialCharacters = []
        part_numbers: PartNumbers = []
        for index, character in enumerate(line):
            if character == ".":
                continue
            try:
                int(character)
            except ValueError:
                special_character_indexes.append(index)
                continue
            try:
                int(line[index + 1])
            except (ValueError, IndexError):
                if wip_index is not None:
                    number = int("".join(line[i] for i in list(range(wip_index, index + 1))))
                    part_numbers.append((number, wip_index, index))
                else:
                    number = int(character)
                    part_numbers.append((number, index, index))
                wip_index = None
                continue
            else:
                if wip_index is None:
                    wip_index = index
                continue
        schematic.append((special_character_indexes, part_numbers))

    valid_part_numbers: list[int] = []

    for index, partial_schematic in enumerate(schematic):  # type: int, PartialSchematic
        special_character_indexes, part_numbers = partial_schematic
        for part_number, start_index, end_index in part_numbers:
            if start_index - 1 in special_character_indexes or end_index + 1 in special_character_indexes:
                valid_part_numbers.append(part_number)
                continue
            if start_index == end_index:
                part_number_range = [start_index - 1, start_index, start_index + 1]
            else:
                part_number_range = list(range(start_index - 1, end_index + 2))
            if index != 0:
                previous_special_character_indexes = schematic[index - 1][0]
                if any(i in previous_special_character_indexes for i in part_number_range):
                    valid_part_numbers.append(part_number)
                    continue
            if (index + 1) != len(schematic):
                next_special_character_indexes = schematic[index + 1][0]
                if any(i in next_special_character_indexes for i in part_number_range):
                    valid_part_numbers.append(part_number)
                    continue

    return sum(valid_part_numbers)


def solve_part_2() -> int:
    ...


def main() -> None:
    part_1_answer: int = solve_part_1()
    print(f"{part_1_answer=}")
    part_2_answer: int = solve_part_2()
    print(f"{part_2_answer=}")


if __name__ == "__main__":
    main()
