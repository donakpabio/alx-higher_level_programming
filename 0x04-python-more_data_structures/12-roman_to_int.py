#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string is not None or len(roman_string) > 0:
        rom = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        v = 0
        for n in range(len(roman_string)):
            if n > 0 and rom[roman_string[n]] > rom[roman_string[n - 1]]:
                v = v + rom[roman_string[n]] - 2 * rom[roman_string[n - 1]]
            else:
                v = v + rom[roman_string[n]]
        return v
    return None


if __name__ == "__main__":
    roman_to_int(roman_string)
