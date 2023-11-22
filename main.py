import random

secret = random.randint(1, 20)

attempts = 0

with open("record.txt", "r") as record_file:
    best_score = int(record_file.read())
    print(f"Record: {best_score}")


while True:
    guess = int(input("Guess the secret number (between 1 and 20): "))
    attempts += 1

    if guess == secret:
        if attempts < best_score:
            with open("record.txt", "w") as record_file:
                record_file.write(str(attempts))

        print("Congratulations, you are right!")
        print(f"It took you {attempts} attempts.")
        break
    elif guess > secret:
        print("Try smaller.")
    elif guess < secret:
        print("Try bigger.")
    else:
        print("Oops, try again!")

