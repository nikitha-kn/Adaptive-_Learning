import random

class PuzzleGenerator:
    def generate(self, difficulty):
        if difficulty == 1:
            a, b = random.randint(1, 10), random.randint(1, 10)
        elif difficulty == 2:
            a, b = random.randint(10, 50), random.randint(10, 50)
        else:
            a, b = random.randint(50, 100), random.randint(50, 100)

        op = random.choice(["+", "-","*", "/"])
        question = f"{a} {op} {b}"
        answer = eval(question)

        return question, answer
