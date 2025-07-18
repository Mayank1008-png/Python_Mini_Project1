import random

# 1. Subjects - Animal characters
animals = [
    "A dancing panda",
    "A confused elephant",
    "A llama",
    "A yoga-practicing cat",
    "A chicken wearing glasses"
]

# 2. Actions - Silly animal activities
actions = [
    "steals a pizza",
    "joins a startup",
    "hacks into NASA",
    "becomes mayor",
    "starts a YouTube channel"
]

# 3. Places or objects - Funny locations/things
places = [
    "at a dog wedding",
    "on a spaceship",
    "inside a vending machine",
    "at the zoo's board meeting",
    "in an auto rickshaw"
]

print(" Welcome to the Animal Fake News Generator ")

while True:
    subject = random.choice(animals)
    action = random.choice(actions)
    place = random.choice(places)
    
    print(f"\nBREAKING NEWS: {subject} {action} {place}!")

    again = input("\nWant another headline? (yes/no): ").strip().lower()
    if again != "yes":
        break

print("\nThanks for laughing with the animals! Goodbye!")



