import art
import random
from game_data import data

#random_A = random.randint(0,49)
#random_B = random.randint(0,49)

def random_no():
    return random.randint(0,49)

def choice(random):
    return f"Compare A: {data[random]['name']}, a {data[random]['description']}, from {data[random]['country']}"


current_score = 0

print(art.logo)

random_A = random_no()
random_B = random_no()
while random_A == random_B:
    random_A = random_no()

print(choice(random_A))
print(art.vs)
print(choice(random_B))

while True:
    user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    if (data[random_A]['follower_count'] > data[random_B]['follower_count'] and user_guess == 'A') or (data[random_A]['follower_count'] < data[random_B]['follower_count'] and user_guess == 'B'):
        current_score += 1
        print("You are right! Current score: ", current_score)
        random_A = random_B
        random_B = random_no()
        while random_A == random_B:
            random_B = random_no()
        print("\n"*20)
        print(choice(random_A))
        print(art.vs)
        print(choice(random_B))
        continue
    else:
        print("You are wrong! Current score: ", current_score)
        break