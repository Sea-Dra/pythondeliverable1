

print("Welcome to GC mini golf!")
the_name = input("What is your name? ")

no_of_holes = int(input(f"Hi, {the_name}! Would you like to play 3 or 6 holes? "))
if no_of_holes == 3:
    hole1 = int(input("How many putts for hole 1?(par: 3) "))
    hole2 = int(input("How many putts for hole 2?(par: 3) "))
    hole3 = int(input("How many putts for hole 3?(par: 3) "))
    total_par = int(hole1 + hole2 + hole3)
    total_score = int(total_par) - 9
    if int(total_score) < 0:
        print(f"Great job, {the_name}! Your total score was: {total_score}")
    elif total_score == 0:
        print(f"Good Game, {the_name}! Your total score was: {total_score}")
    elif total_score > 0:
        print(f"Nice try, {the_name}! Your total score was: +{total_score}")
elif no_of_holes == 6:
    hole1 = int(input("How many putts for hole1?(par: 3) "))
    hole2 = int(input("How many putts for hole 2?(par: 3) "))
    hole3 = int(input("How many putts for hole 3?(par: 3) "))
    hole4 = int(input("how many putts for hole 4?(par: 3) "))
    hole5 = int(input("How many putts for hole 5?(par: 3) "))
    hole6 = int(input("How many putts for hole 6?(par: 3) "))
    total_par = int(hole1 + hole2 + hole3 + hole4 + hole5 + hole6)
    total_score = (total_par - 18)
    if int(total_score) < 0:
        print(f"Great job, {the_name}! Your total score was: {total_score}")
    elif int(total_score) == 0:
        print(f"Good Game, {the_name}! Your total score was: {total_score}")
    elif total_score > 0:
        print(f"Nice try, {the_name}! Your total score was: +{total_score}")
else:
        print(f"{no_of_holes} is an invalid option")
