from datetime import datetime, timezone

# Function for converting UNIX timestamps to datetime values.
def convert_seconds(unix_seconds):
    # Ensure the timestamp is treated as seconds (with fractional seconds for millisecond precision)
    dt = datetime.fromtimestamp(unix_seconds, tz=timezone.utc)
    return dt.isoformat()

def clean_text(text):
    # Step 1: Find the first instance of "\n\n>" and remove everything after it
    cutoff_index = text.find("\n\n>")
    if cutoff_index != -1:  # If "\n\n>" was found
        text = text[:cutoff_index]
        
        # Step 2: From the end, find the first instance of "\n" and remove everything after that
        # This step only occurs if "\n\n>" was found
        last_line_index = text.rfind("\n")
        if last_line_index != -1 and last_line_index != 0:  # Ensure "\n" was found and it's not at the start
            text = text[:last_line_index]
    # If "\n\n>" was not found, do nothing and keep the text as is

    return text