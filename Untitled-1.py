def roman_to_int(s: str) -> int:
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    
    for char in reversed(s):
        value = roman_values.get(char, 0)
        if value == 0:
            raise ValueError("Некоректне римське число")
        total = total - value if value < prev_value else total + value
        prev_value = value
    
    return total

if __name__ == "__main__":
    try:
        roman_number = input("Введіть римське число: ").strip().upper()
        print("Арабське число:", roman_to_int(roman_number))
    except ValueError as e:
        print(e)
