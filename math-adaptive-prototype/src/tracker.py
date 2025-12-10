import time

class PerformanceTracker:
    def __init__(self):
        self.correct = 0
        self.total = 0
        self.times = []

    def record(self, correct, time_taken):
        self.total += 1
        if correct:
            self.correct += 1
        self.times.append(time_taken)

    def summary(self):
        accuracy = (self.correct / self.total) * 100 if self.total else 0
        avg_time = sum(self.times) / len(self.times) if self.times else 0

        return accuracy, avg_time
