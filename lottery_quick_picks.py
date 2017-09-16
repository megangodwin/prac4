import random

def main():
    global num_picks
    valid_number = False
    while not valid_number:
        try:
            num_picks = int(input("How many quick picks: "))
            valid_number = True
        except ValueError:
            print("Enter valid number")

    for num in range(num_picks):
        picks = [random.randint(0, 45) for num in range(6)]
        print(picks)
main()
