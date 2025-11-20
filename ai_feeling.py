# AI Emotion Detection in Python
# Requires: pip install transformers torch

from transformers import pipeline
import sys

def detect_emotion(text: str) -> dict:
    """
    Detects the emotion of a given text using a pre-trained model.
    Returns the top predicted emotion and its confidence score.
    """
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Input must be a non-empty string.")

    # Load the emotion classification pipeline
    # Model: 'j-hartmann/emotion-english-distilroberta-base'
    classifier = pipeline(
        "text-classification",
        model="j-hartmann/emotion-english-distilroberta-base",
        return_all_scores=True
    )

    # Get predictions
    results = classifier(text)[0]

    # Sort by confidence
    results_sorted = sorted(results, key=lambda x: x['score'], reverse=True)
    top_emotion = results_sorted[0]

    return {
        "emotion": top_emotion['label'],
        "confidence": round(top_emotion['score'] * 100, 2),
        "all_scores": results_sorted
    }

if __name__ == "__main__":
    try:
        # If run from terminal, allow user input
        if len(sys.argv) > 1:
            user_text = " ".join(sys.argv[1:])
        else:
            user_text = input("Enter a sentence to analyze emotion: ")

        result = detect_emotion(user_text)
        print(f"Detected Emotion: {result['emotion']} ({result['confidence']}% confidence)")
        print("All scores:")
        for r in result['all_scores']:
            print(f"  {r['label']}: {round(r['score']*100, 2)}%")

    except Exception as e:
        print(f"Error: {e}")
