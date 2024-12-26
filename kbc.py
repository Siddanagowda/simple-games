question = [
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Saturn", 2],
    ["What is the capital of France?", "Berlin", "Madrid", "Paris", "Lisbon", 3],
    ["Who wrote 'Hamlet'?", "Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen", 2],
    ["What is the largest ocean on Earth?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", 4],
    ["Which element has the chemical symbol 'O'?", "Oxygen", "Gold", "Silver", "Iron", 1],
    ["What is the hardest natural substance on Earth?", "Gold", "Iron", "Diamond", "Platinum", 3],
    ["Who painted the Mona Lisa?", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet", 3],
    ["What is the smallest country in the world?", "Vatican City", "Monaco", "Nauru", "San Marino", 1],
    ["Which is the longest river in the world?", "Amazon", "Nile", "Yangtze", "Mississippi", 2],
    ["What is the capital of Japan?", "Seoul", "Beijing", "Tokyo", "Bangkok", 3],
    ["Who discovered penicillin?", "Marie Curie", "Alexander Fleming", "Isaac Newton", "Albert Einstein", 2],
    ["What is the largest desert in the world?", "Sahara", "Arabian", "Gobi", "Kalahari", 1],
    ["Which is the smallest planet in our solar system?", "Mercury", "Venus", "Earth", "Mars", 1]
]

levels = [1000, 2000, 3000, 4000, 5000, 10000, 20000, 30000, 40000, 50000, 100000, 500000, 10000000]
base_levels = [1000,2000,3000,4000,5000, 10000, 50000, 100000, 1000000]

money = 0
last_base_level = 0

for i in range(len(question)):
    questions = question[i]
    print(f"Question for Rs.{levels[i]}")
    print(f"{questions[0]}")
    print(f"a. {questions[1]}  b. {questions[2]}")
    print(f"c. {questions[3]}  d. {questions[4]}")
    reply = int(input("Enter your answer (1-4): "))

    if reply == questions[-1]:
        money = levels[i]
        print(f"Correct answer! You won Rs.{levels[i]}\n\n")
        if money in base_levels:
            last_base_level = money
            print(f"Congratulations! You have reached a base level of Rs.{money}. You cannot lose this amount.\n")
    else:
        print("Wrong answer!\n\n")
        money = last_base_level
        break

print(f"\n---------\nYou won Rs.{money}\n---------\n")