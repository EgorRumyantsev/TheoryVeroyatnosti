import random

def roll_dice():
    return random.randint(1, 6)

def simulate_dice_rolls(num_rolls):
    results = {}
    for _ in range(num_rolls):
        total = sum([roll_dice() for _ in range(2)])  # Change the number inside range to simulate different number of dice rolls
        if total in results:
            results[total] += 1
        else:
            results[total] = 1

    for key in sorted(results.keys()):
        frequency = results[key] / num_rolls * 100
        print(f'Sum {key} occurred with frequency {frequency:.2f}%')

simulate_dice_rolls(1000000)
