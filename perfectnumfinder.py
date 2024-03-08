import json
from decimal import Decimal, getcontext

# Set precision to handle large numbers
getcontext().prec = 10001

def is_perfect_number(num):
    divisors = [1]
    for i in range(2, int(num.sqrt()) + 1):
        if num % i == 0:
            divisors.extend([i, num // i])
    return sum(divisors) == num

def save_current_number(num):
    # Save the current checked number in a separate JSON file
    with open('current_checked_number.json', 'w', encoding='utf-8') as file:
        json.dump({'current_checked_number': str(num)}, file)

def save_odd_perfect_number(num):
    # Save the odd perfect number in a separate JSON file
    with open('odd_perfect_number.json', 'w', encoding='utf-8') as file:
        json.dump({'odd_perfect_number': str(num)}, file)

def find_odd_perfect_number(starting_num):
    try:
        # Attempt to load the current checked number from the file
        with open('current_checked_number.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            num = Decimal(data['current_checked_number'])
    except (FileNotFoundError, json.JSONDecodeError):
        # If file not found or decoding issue, use the starting number
        num = Decimal(starting_num)

    while True:
        print(f'Checking: {num}')
        if num % 2 == 1 and is_perfect_number(num):
            print(f'Odd perfect number found: {num}')
            # Save the odd perfect number
            save_odd_perfect_number(num)
            break
        num += 2  # Increment by 2 to check odd numbers only

        # Save the current checked number periodically or on termination
        save_current_number(num)

# Start checking from 10^10000
find_odd_perfect_number(10**10000)
