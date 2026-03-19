# utils.py

from ai_integration import get_ai_suggestions

def analyze_code(code, checklist):
    """
    Analyzes the given code against the checklist and returns observations and suggestions.
    
    Args:
    - code (str): The code to be analyzed.
    - checklist (str): The list of quality checks.
    
    Returns:
    - observations (list): A list of observations based on the checklist.
    - suggestions (list): A list of improvement suggestions based on AI feedback.
    """
    
    # Get AI suggestions from the integration function
    ai_feedback = get_ai_suggestions(code, checklist)
    
    # Split the feedback into observations and suggestions (you can improve this part if necessary)
    observations = []
    suggestions = []

    # Process the feedback (for now, we split into two sections)
    feedback_lines = ai_feedback.split("\n")
    
    for line in feedback_lines:
        if line.strip().startswith("Observations"):
            observations.append(line)
        elif line.strip().startswith("Suggestions"):
            suggestions.append(line)
        else:
            if line.strip():
                observations.append(line)  # Assume anything else is an observation
    
    return observations, suggestions