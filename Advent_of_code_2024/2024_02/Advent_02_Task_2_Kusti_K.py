import numpy as np

def is_safe_report(report):
    # Convert the report to a numpy array for easy calculation of differences
    levels = np.array(report)
    
    # Calculate the differences between adjacent levels
    diffs = np.diff(levels)
    
    # Check if all differences are between 1 and 3, and if all differences are either increasing or decreasing
    if np.all(np.abs(diffs) >= 1) and np.all(np.abs(diffs) <= 3):
        # Check if all differences are either non-negative (increasing) or non-positive (decreasing)
        if np.all(diffs >= 0) or np.all(diffs <= 0):
            return True
    return False

def is_safe_report_after_removal(report):
    # Try removing each level and check if the resulting report is safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]  # Remove the level at index i
        if is_safe_report(modified_report):
            return True
    return False

def count_safe_reports_from_file(file_path):
    safe_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            # Parse each line into a list of integers
            report = list(map(int, line.split()))
            # Check if the report is safe without any modification or if it can become safe by removing one level
            if is_safe_report(report) or is_safe_report_after_removal(report):
                safe_count += 1
    return safe_count

# Example usage
file_path = 'input.txt'  # Replace with the actual path to the file
safe_reports = count_safe_reports_from_file(file_path)
print(safe_reports)
