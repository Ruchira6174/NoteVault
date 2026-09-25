from typing import List, Dict, Any

def generate_mcqs(text: str) -> List[Dict[str, Any]]:
    """Generate 10 multiple-choice questions based on the text."""
    # TODO: Call LLM to generate quiz
    return [
        {
            "question": f"Question {i}",
            "options": ["Option A", "Option B", "Option C", "Option D"],
            "correct_answer": "Option A",
            "explanation": "Because it is the mock answer."
        }
        for i in range(1, 11)
    ]
