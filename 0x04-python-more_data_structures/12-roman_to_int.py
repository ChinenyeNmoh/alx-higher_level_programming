#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    value = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    result = 0
    i = 0

    while i < len(roman_string):
        curr = value.get(roman_string[i])

        if i + 1 < len(roman_string):
            next_val = value.get(roman_string[i + 1])

            if curr >= next_val:
                result += curr
                i += 1
            else:
                result += (next_val - curr)
                i += 2
        else:
            result += curr
            i += 1

    return result
