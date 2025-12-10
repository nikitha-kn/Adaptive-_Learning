from puzzle_generator import PuzzleGenerator
from tracker import PerformanceTracker
from adaptive_engine import AdaptiveEngine
import time

print("Welcome to Adaptive Math Learning!")
name = input("Enter your name: ")

generator = PuzzleGenerator()
tracker = PerformanceTracker()
engine = AdaptiveEngine()

print("\nStarting with Easy difficulty...\n")

for i in range(8):
    difficulty = engine.difficulty

    print(f"\nCurrent Difficulty: {difficulty}")

    ques, ans = generator.generate(difficulty)

    print(f"Q{i+1}: Solve → {ques}")
    start = time.time()
    user_ans = int(input("Your answer: "))
    end = time.time()

    correct = (user_ans == ans)
    tracker.record(correct, end - start)

    if correct:
        print(" Correct!")
    else:
        print(f" Wrong! Correct answer was {ans}")

    engine.update(correct)

print("\n===== SUMMARY =====")
acc, avg_time = tracker.summary()

print(f"Student: {name}")
print(f"Accuracy: {acc:.2f}%")
print(f"Avg Time: {avg_time:.2f} sec")
print(f"Next Recommended Level: {engine.difficulty}")

print("\nThanks for playing!")
