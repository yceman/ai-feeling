class AIFeeling:
    def __init__(self):
        self.state = {"happy": 0.5, "sad": 0.2, "curious": 0.7}

    def update_feeling(self, feeling, intensity):
        if feeling in self.state:
            self.state[feeling] = intensity

    def dominant_feeling(self):
        return max(self.state, key=self.state.get)

ai = AIFeeling()
ai.update_feeling("happy", 0.9)
print("Dominant feeling:", ai.dominant_feeling())

