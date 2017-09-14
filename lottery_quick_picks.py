import random

def main():
    valid_number = False
    while not valid_number:
        try:
            num_picks = int(input("How many quick picks: "))
            valid_number = True
        except ValueError:
            print("Enter valid number")

    for picks in num_picks:
        pick_gen = [picks.randrange(1, 46) for picks in range(0, 6)]
        print(pick_gen)
main()
