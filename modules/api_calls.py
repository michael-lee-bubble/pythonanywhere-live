from datetime import datetime, timezone

# Function for converting UNIX timestamp in milliseconds to a datetime string.
def convert_milliseconds(unix_milliseconds):
    # Convert milliseconds to seconds (including fractional part for milliseconds)
    seconds = unix_milliseconds / 1000.0
    # Create a timezone-aware datetime object from the timestamp (in UTC)
    dt = datetime.fromtimestamp(seconds, tz=timezone.utc)
    # Return the datetime in ISO 8601 format, ensuring milliseconds are included
    return dt.isoformat()
