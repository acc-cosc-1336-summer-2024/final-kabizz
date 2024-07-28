def calculate_statistics(numbers):
    """Calculates and returns statistics for a list of numbers."""
    if not numbers:
        raise ValueError("The list is empty.")

    lowest = min(numbers)
    highest = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)
    
    return lowest, highest, total, average