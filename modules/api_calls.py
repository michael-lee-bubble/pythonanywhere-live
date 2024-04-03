from datetime import datetime, timezone

# Function for converting UNIX timestamps to datetime values.
def convert_seconds(unix_seconds):
    # Ensure the timestamp is treated as seconds (with fractional seconds for millisecond precision)
    dt = datetime.fromtimestamp(unix_seconds, tz=timezone.utc)
    return dt.isoformat()

def clean_text(text):
    # Define initial patterns with a tuple indicating the pattern and the method to use: (pattern, method)
    initial_patterns = [("\n\n>", "find"), ("\n", "rfind"), (" Bubble Support - ", "rfind"), ("\n", "rfind")]

    # Special case patterns with the same structure for consistency
    special_patterns = [("How was the help you received?\n>", "rfind"), ("\n", "rfind")]

    # Function to process patterns with specified method (find or rfind)
    def process_patterns(text, patterns):
        for pattern, method in patterns:
            cutoff_index = text.rfind(pattern) if method == "rfind" else text.find(pattern)
            if cutoff_index > 0:  # Check if pattern is found and it's not at the very start
                return text[:cutoff_index], True  # Return truncated text and flag indicating further processing
        return text, False  # No pattern found or it's at the start; no further processing

    # Process initial patterns
    process_further = True
    while process_further:
        text, process_further = process_patterns(text, initial_patterns)
    
    # Process special case patterns with conditional processing
    for pattern, method in special_patterns:
        text, found = process_patterns(text, [(pattern, method)])
        if not found:
            # If the first special pattern isn't found, don't continue to the second
            break

    return text