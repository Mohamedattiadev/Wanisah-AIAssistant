# tools/calculator.py
import re

def calculate(query):
    """Evaluates a simple mathematical expression from a query string."""
    # Sanitize and find the mathematical expression
    query = query.replace("what is", "").replace("calculate", "").strip()
    # Allow numbers, spaces, and basic operators + - * / . ( )
    if not re.match(r"^[0-9\s\.\+\-\*\/\(\)]+$", query):
        return "I can only handle simple mathematical expressions, sir."

    try:
        # Use eval in a very restricted way for safety
        result = eval(query, {"__builtins__": None}, {})
        return f"The result is {result}."
    except Exception as e:
        print(f"Calculation error: {e}")
        return "I'm sorry, sir, I couldn't calculate that."
