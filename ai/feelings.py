# Simple emotion model
ai_feelings = {
    "happy": 0.8,
    "sad": 0.1,
    "angry": 0.05,
    "curious": 0.6
}

# Example: check dominant feeling
dominant = max(ai_feelings, key=ai_feelings.get)
print(f"The AI is mostly feeling {dominant}.")
