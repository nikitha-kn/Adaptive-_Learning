class AdaptiveEngine:
    def __init__(self):
        self.difficulty = 1
        self.correct = 0
        self.wrong = 0

    def update(self, was_correct):
        if was_correct:
            self.correct += 1
            self.wrong = 0
        else:
            self.wrong += 1
            self.correct = 0

        if self.correct == 2:
            self.difficulty = min(3, self.difficulty + 1)
            self.correct = 0

        if self.wrong == 2:
            self.difficulty = max(1, self.difficulty - 1)
            self.wrong = 0

        return self.difficulty
