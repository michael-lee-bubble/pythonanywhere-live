from datetime import datetime, timezone

# Function for converting UNIX timestamps to datetime values.
def convert_seconds(unix_seconds):
    # Ensure the timestamp is treated as seconds (with fractional seconds for millisecond precision)
    dt = datetime.fromtimestamp(unix_seconds, tz=timezone.utc)
    return dt.isoformat()

def clean_text(text):
    # Step 1: Find the first instance of "\n\n>" and remove everything after it
    cutoff_index_1 = text.find("\n\n>")
    if cutoff_index_1 != -1:  # If "\n\n>" was found
        text = text[:cutoff_index_1]
        
        # Step 2: From the end, find the first instance of "\n" and remove everything after that
        # This step only occurs if "\n\n>" was found
        cutoff_index_2 = text.rfind("\n")
        if cutoff_index_2 != -1 and cutoff_index_2 != 0:  # Ensure "\n" was found and it's not at the start
            text = text[:cutoff_index_2]
            
            # Find additional text to remove
            cutoff_index_3 = text.rfind(" Bubble Support - ") # If " Bubble Support - " was found
            if cutoff_index_3 != -1:
                text = text[:cutoff_index_3]

                # Find additional text to remove
                cutoff_index_4 = text.rfind("\n")
                if cutoff_index_4 != -1 and cutoff_index_4 != 0:  # Ensure "\n" was found and it's not at the start
                    text = text[:cutoff_index_4]

    rating_text_index = text.find("How was the help you received?\n>")
    if rating_text_index != -1:  # If "How was the help you received?\n>" was found
        text = text[:rating_text_index]

        # Find additional text to remove
        cutoff_index_5 = text.rfind("\n")
        if cutoff_index_5 != -1 and cutoff_index_5 != 0:
            text = text[:cutoff_index_5]

    return text