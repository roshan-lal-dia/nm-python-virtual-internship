def roman_to_int(roman_numeral):
    roman_dict = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}
    int_val = 0
    for i in range(len(roman_numeral)):
        if i > 0 and roman_dict[roman_numeral[i].lower()] > roman_dict[roman_numeral[i - 1].lower()]:
            int_val += roman_dict[roman_numeral[i].lower()] - 2 * roman_dict[roman_numeral[i - 1].lower()]
        else:
            int_val += roman_dict[roman_numeral[i].lower()]
    return int_val

roman_numeral = input("Enter a Roman numeral: ")
integer_value = roman_to_int(roman_numeral)
print(f"The integer value of {roman_numeral.upper()} is {integer_value}")
