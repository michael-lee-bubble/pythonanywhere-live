from datetime import datetime
import pytz

# Function for converting UNIX to a datetime.
def convert_milliseconds(unix):
    seconds = unix / 1000.0
    dt = datetime.utcfromtimestamp(seconds).replace(tzinfo=pytz.utc)
    return dt.isoformat()