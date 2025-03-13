#!/bin/python3
### FOR ETHICAL PURPOSES ONLY ###
### But idk how you would use it unetically if I'm being honest ###

### This tool is designed for those situations where your network security tools discover possible credit card numbers. Use this tool to validate findings as true/false positives ###
### https://github.com/EmotionalSupportWaterBottle ###

def luhn_check(card_number):
    card_number = card_number.replace(" ", "").replace("-", "")  # Remove spaces and dashes
    if not card_number.isdigit():
        return "Invalid input: Only digits, spaces, and dashes are allowed."

    digits = [int(d) for d in card_number]
    checksum = 0
    is_second = False

    # Process digits from right to left
    for i in range(len(digits) - 1, -1, -1):
        d = digits[i]
        if is_second:
            d *= 2
            if d > 9:
                d -= 9
        checksum += d
        is_second = not is_second

    return "Valid credit card number!" if checksum % 10 == 0 else "Invalid credit card number."

# Example usage
card_number = input("Enter the credit card number: ")
print(luhn_check(card_number))
