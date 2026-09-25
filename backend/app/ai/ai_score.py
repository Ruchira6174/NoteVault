from typing import Dict, Any

def calculate_final_score(metrics: Dict[str, Any]) -> Dict[str, Any]:
    """Combine all evaluations into one final score."""
    accuracy = metrics.get("accuracy", 0.0)
    originality = metrics.get("originality", 0.0)
    readability = metrics.get("readability", 0.0)
    syllabus = metrics.get("syllabus", 0.0)
    
    overall_score = (accuracy * 0.4) + (originality * 0.3) + (readability * 0.15) + (syllabus * 0.15)
    
    return {
        "overall_score": round(overall_score, 1),
        "accuracy_score": accuracy,
        "originality_score": originality,
        "readability_score": readability,
        "syllabus_coverage": syllabus,
        "recommendation": "Highly Recommended" if overall_score >= 85.0 else "Needs Improvement"
    }
