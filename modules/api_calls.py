from datetime import datetime, timezone

# Function for converting UNIX timestamps to datetime values.
def convert_seconds(unix_seconds):
    # Ensure the timestamp is treated as seconds (with fractional seconds for millisecond precision)
    dt = datetime.fromtimestamp(unix_seconds, tz=timezone.utc)
    return dt.isoformat()
